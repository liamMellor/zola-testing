package com.cafe.noir.panels;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.event.EventTarget;
import javafx.scene.Node;
import javafx.scene.control.ContextMenu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TreeCell;
import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.ClipboardContent;
import javafx.scene.input.DataFormat;
import javafx.scene.input.DragEvent;
import javafx.scene.input.Dragboard;
import javafx.scene.input.MouseEvent;
import javafx.scene.input.TransferMode;
import javafx.stage.Stage;

import com.cafe.noir.dialogs.SaveDialog;
import com.cafe.noir.dialogs.SaveDialog.Response;
import com.cafe.noir.directeur.DirecteurCenterPanel;
import com.cafe.noir.directeur.DirecteurLeftPanel;
import com.cafe.noir.directeur.OnDeleteListener;
import com.cafe.noir.directeur.OnRightClickListener;
import com.cafe.noir.directeur.PanelPos;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.manager.FileManager;

public class DragAndDropCell extends TreeCell<File>
{
    private File item;
	public TreeView<File> parentTree;
	private TreeView<File> targetTree;
	
	private File newFolderPath;

	final PanelPos panelPos;

    public DragAndDropCell( final TreeView<File> parentTree, final PanelPos panelPos ) 
    {
        this.parentTree = parentTree;
        this.panelPos = panelPos;
                
        setOnDragDetected( new EventHandler<MouseEvent>() 
		{
            @Override
            public void handle( MouseEvent event ) 
            {

                if ( item == null ) 
                {
                    return;
                }
                
                Dragboard dragBoard = startDragAndDrop( TransferMode.MOVE );
                ClipboardContent content = new ClipboardContent();
                ObservableList<TreeItem<File>> selectedItems = parentTree.getSelectionModel().getSelectedItems();
                ArrayList<File> selectedItemStrings = new ArrayList<File>();
                for( TreeItem<File> selectedItem : selectedItems )
                {
                	selectedItemStrings.add( selectedItem.getValue() );
                }
                content.put( DataFormat.FILES, selectedItemStrings );
                dragBoard.setContent( content );
                
                event.consume();
            }
        });
        setOnDragDone(new EventHandler<DragEvent>() 
		{
            @Override
            public void handle( DragEvent dragEvent ) 
            {
                dragEvent.consume();
            }
        });
        
        setOnDragOver(new EventHandler<DragEvent>() 
		{
            @Override
            public void handle( DragEvent dragEvent ) 
            {            	
                setTarget( dragEvent.getTarget() );
                
                DragAndDropCell dCell =  getDragAndDropCell( ((Node)dragEvent.getTarget()) );
                
                dCell.getStyleClass().add( "drag-hover" );
                
                dragEvent.acceptTransferModes( TransferMode.MOVE );
                        
                dragEvent.consume();
            }
        });
        setOnDragExited( new EventHandler<DragEvent>()
		{
			@Override
			public void handle( DragEvent dragEvent ) 
			{
				DragAndDropCell dCell =  (DragAndDropCell) ((Node)dragEvent.getTarget());
                
                dCell.getStyleClass().remove( dCell.getStyleClass().size() - 1 );
			}
	
		});
        setOnDragDropped( new EventHandler<DragEvent>() 
		{
    		@SuppressWarnings("unchecked")
            @Override
            public void handle( DragEvent dragEvent ) 
            {
            	if( panelPos == PanelPos.CENTER && getTarget().getId().equals( "centerTree" ) )
            	{
					ArrayList<File> valuesToMove = (ArrayList<File>) dragEvent.getDragboard().getContent( DataFormat.FILES );
					for( File valueToMove : valuesToMove )
                    {
						TreeItem<File> itemToMove = new TreeItem<File>( valueToMove );
	                    itemToMove.setExpanded( true );
	                    // Add to new parent.
	                    getTarget().getRoot().getChildren().add( itemToMove );
                    }
            	}
            	else if( panelPos == PanelPos.LEFT && getTarget().getId().equals( "leftTree" ) )
            	{
            		DragAndDropCell dCell = getDragAndDropCell( ((Node)dragEvent.getTarget()) );
            		if( dCell.getTreeItem().getValue().isDirectory() )
            		{
    					ArrayList<File> valuesToMove = (ArrayList<File>) dragEvent.getDragboard().getContent( DataFormat.FILES );
    					for( File valueToMove : valuesToMove )
                        {
    						searchAndRemoveLeaves( DirecteurLeftPanel.treeView.getRoot().getChildren(), valueToMove );
    						TreeItem<File> itemToMove = new TreeItem<File>( valueToMove );
    						try 
    						{
								FileManager.copyFile( 
										valueToMove, 
										new File( dCell.getTreeItem().getValue() + File.separator + valueToMove.getName() ) 
										);
								if( valueToMove.isDirectory() )
								{
									for( File values : valueToMove.listFiles() )
									{
										values.delete();
									}
								}
								valueToMove.delete();
							} 
    						catch ( IOException e ) 
    						{
								e.printStackTrace();
							}
    						
    						valueToMove.delete();
    	                    itemToMove.setExpanded( true );

    	                    dCell.getTreeItem().getChildren().addAll( itemToMove );
    	                    DirecteurLeftPanel.notifyDataSetChanged();
                        }
            		}
            	}
            	else
            	{
            		TreeItem<File> itemToRemove = null;
            		for( TreeItem<File> itemQuery : DirecteurCenterPanel.treeView.getRoot().getChildren() )
            		{
            			for( File f : dragEvent.getDragboard().getFiles() )
            			{
            				if( itemQuery.getValue().equals( f ) )
                			{
                				itemToRemove = itemQuery;
                				break;
                			}
            			}
            		}
            		if( itemToRemove != null ) DirecteurCenterPanel.treeView.getRoot().getChildren().remove( itemToRemove );
            	}
                dragEvent.consume();
            }
        });
    }
    private DragAndDropCell getDragAndDropCell( Node targ )
    {
		if( targ instanceof DragAndDropCell )
			return ((DragAndDropCell)targ );
		else
			return getDragAndDropCell( targ.getParent() );	
    }
    
    private void searchAndRemoveLeaves( ObservableList<TreeItem<File>> observableList, File fileToMatch )
    {
    	for( TreeItem<File> itemQuery : observableList )
		{
			if( !itemQuery.getValue().isDirectory() )
			{
				if( itemQuery.getValue().getAbsolutePath().equals( fileToMatch.getAbsolutePath() ) )
				{
					itemQuery.getParent().getChildren().remove( itemQuery );
					break;
				}
			}
			else
				searchAndRemoveLeaves( itemQuery.getChildren(), fileToMatch );
		}
    }
    private void setTarget( EventTarget eventTarget )
    {
    	if( ((Node)eventTarget).getParent() instanceof DragAndDropCell )
    		targetTree = ((DragAndDropCell)((Node)eventTarget).getParent()).parentTree;
    	else
    		targetTree = ((DragAndDropCell)((Node)eventTarget).getParent().getParent()).parentTree;
    }
    
    private TreeView<File> getTarget()
    {
    	return targetTree;
    }
    
    @Override
    protected void updateItem( File item, boolean empty ) 
    {
        super.updateItem( item, empty );
        this.item = item;
        String text = ( item == null ) ? null : item.getName();
        setText( text );
        
        setOnMouseClicked( new OnRightClickListener( parentTree, this ) );
        setContextMenu( cMenu() );
        
        if( text != null && text.equals( "selenium" ) )
        {
        	setText( "Selenium" );
        	setGraphic( new ImageView( new Image( getClass().getResourceAsStream( "/img/sel_icn.png" ), 25, 25, true, true ) ) );
        }
        else if ( text != null && text.equals( "cgi" ) )
        {
        	setText( "API" );
        	setGraphic( new ImageView( new Image( getClass().getResourceAsStream( "/img/api_icn.png" ), 30, 30, true, true ) ) );
        }
        else if ( text != null && item.isDirectory() )
        	setGraphic( new ImageView( new Image( getClass().getResourceAsStream( "/img/folder_icn.png" ), 25, 25, true, true ) ) );
    }
    
    private ContextMenu cMenu()
	{
		ContextMenu c = new ContextMenu();
		MenuItem addFolder = new MenuItem( "Add Folder" );
		MenuItem deleteItem = new MenuItem( "Delete" );
		
		addFolder.setOnAction( new EventHandler<ActionEvent>()
		{
			@Override
			public void handle( ActionEvent arg0 ) 
			{
				List<? extends Object> resp = SaveDialog.showConfirmDialog( new Stage(), "Please select a name for your folder.", "Save", FrameType.Manager );
				switch( ((Response)resp.get( 0 )) )
				{
					case CANCEL:
						break;
					case NO:
						break;
					case YES:
						FileManager.createDir( new File( getContextMenuFolderPath() + File.separator + ((String)resp.get( 1 )) ) );
						break;
					default:
						break;
				}
			}
		});
		
		deleteItem.setOnAction( new OnDeleteListener( getTreeView() ) );
		c.getItems().addAll( addFolder, deleteItem );
		return c;
	}
	
	public void setContextMenuFolderPath( File file )
	{
		this.newFolderPath = file;
	}
	public File getContextMenuFolderPath()
	{
		return this.newFolderPath;
	}
}