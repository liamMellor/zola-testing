package com.cafe.noir.directeur;

import java.io.File;
import java.util.Arrays;
import java.util.List;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.SelectionMode;
import javafx.scene.control.TreeCell;
import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.util.Callback;

import com.cafe.noir.panels.DragAndDropCell;
import com.cafe.noir.util.NoirStyleUtilities;
import com.cafe.noir.util.manager.ArriereDataManager;
import com.cafe.noir.util.manager.AvantDataManager;

public class DirecteurLeftPanel extends BorderPane
{
    static TreeItem<File> dummyRoot = new TreeItem<File>();

    static File[] folders = new File[]{ ArriereDataManager.cgiDir, AvantDataManager.selDir };

	public static TreeView<File> treeView;
    
	public DirecteurLeftPanel()
	{
		super();
		
		if( !ArriereDataManager.cgiDir.exists() )
			ArriereDataManager.cgiDir.mkdirs();
		if( !AvantDataManager.selDir.exists() )
			AvantDataManager.selDir.mkdirs();
		
		treeView = new TreeView<File>( dummyRoot );
		treeView.setId( "leftTree" );
		
		treeView.setCellFactory( new Callback<TreeView<File>, TreeCell<File>>() 
		{
            @Override
            public TreeCell<File> call( TreeView<File> param ) 
            {
                return new DragAndDropCell( param, PanelPos.LEFT );
            }
        });
		
		TreeItem<File> seleniumRootItem = new TreeItem<File> ( folders[1] );
		
        seleniumRootItem.setExpanded( true );
        
        TreeItem<File> cgiRootItem = new TreeItem<File> ( folders[0] );
		
        cgiRootItem.setExpanded( true );
        
        listFilesForFolder( Arrays.asList( cgiRootItem, seleniumRootItem ) );
		        
        dummyRoot.getChildren().addAll( Arrays.asList( seleniumRootItem, cgiRootItem ) );

        treeView.getSelectionModel().setSelectionMode( SelectionMode.MULTIPLE );
        
        treeView.setShowRoot( false );
        
        treeView.setPrefWidth( 500 );
                        
        setCenter( treeView );
        setBottom( buttonPane() );
	}
	
	private HBox buttonPane()
    {      
    	Button editButton = new Button( "Edit" );
    	Button deleteButton = new Button( "Delete" );
    	
    	editButton.setOnMouseClicked( new OnEditListener( treeView ) );
    	deleteButton.setOnAction( new OnDeleteListener( treeView ) );
    	
        NoirStyleUtilities.iPhoneButtonStyle( editButton, deleteButton );
        
    	HBox buttonPane = new HBox();
        buttonPane.setPadding( new Insets( 15, 12, 15, 12 ) );
    	buttonPane.setSpacing( 60 );
        buttonPane.setAlignment( Pos.CENTER );
                
        buttonPane.getChildren().addAll( editButton, deleteButton );
                
        return buttonPane;
    }
	
	public static void notifyDataSetChanged()
	{
		List<TreeItem<File>> childList = Arrays.asList( dummyRoot.getChildren().get( 1 ), dummyRoot.getChildren().get( 0 ) );
		for( TreeItem<File> child : childList )
		{
			child.getChildren().removeAll( child.getChildren() );
		}
		listFilesForFolder( Arrays.asList( dummyRoot.getChildren().get( 1 ), dummyRoot.getChildren().get( 0 ) ) );
	}
	
	public static void listFilesForFolder( List<TreeItem<File>> list )
    {
		for( TreeItem<File> branch : list )
		{
			for( File fileEntry : branch.getValue().listFiles() )
			{
				if( fileEntry.isDirectory() )
	            {
					TreeItem<File> item = new TreeItem<File>( fileEntry );
                	item.setExpanded( true );
                	branch.getChildren().add( item );
                	listFilesForFolder ( Arrays.asList( item ) );
	            }
				else
				{
					TreeItem<File> item = new TreeItem<File>( fileEntry );
                	branch.getChildren().add( item );
				}
			}
		}
    }
	public static void updateViewForFolder( List<TreeItem<File>> list )
	{
		
	}
}
