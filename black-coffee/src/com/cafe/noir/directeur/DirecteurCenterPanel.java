package com.cafe.noir.directeur;

import java.io.File;

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

public class DirecteurCenterPanel extends BorderPane
{
    static TreeItem<File> dummyRoot = new TreeItem<File>();
	private Button runButton = new Button( "Run" );
	public static TreeView<File> treeView;

	public DirecteurCenterPanel() 
	{
		treeView = new TreeView<File>( dummyRoot );
		treeView.setId( "centerTree" );
		
		treeView.setCellFactory( new Callback<TreeView<File>, TreeCell<File>>() 
		{
            @Override
            public TreeCell<File> call( TreeView<File> param ) 
            {
                return new DragAndDropCell( param, PanelPos.CENTER );
            }
        });
        
        treeView.setPrefWidth( 500 );

        treeView.setShowRoot( false );

        treeView.getSelectionModel().setSelectionMode( SelectionMode.MULTIPLE );
        
        setCenter( treeView );
        setBottom( buttonPane() );
	}
	
	public Button getRunButton()
	{
		return runButton;
	}
	
	public TreeView<File> getListModel()
	{
		return treeView;
	}
	
	private HBox buttonPane()
    {      
        NoirStyleUtilities.iPhoneButtonStyle( runButton );
        
    	HBox buttonPane = new HBox();
        buttonPane.setPadding( new Insets( 15, 12, 15, 12 ) );
    	buttonPane.setSpacing( 60 );
        buttonPane.setAlignment( Pos.CENTER );
                
        buttonPane.getChildren().addAll( runButton );
                
        return buttonPane;
    }
}
