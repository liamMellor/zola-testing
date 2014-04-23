package com.cafe.noir.directeur;

import java.io.File;

import com.cafe.noir.panels.DragAndDropCell;

import javafx.event.EventHandler;
import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import javafx.scene.input.MouseButton;
import javafx.scene.input.MouseEvent;

public class OnRightClickListener implements EventHandler<MouseEvent>
{
	private TreeView<File> treeView;
	private DragAndDropCell dragAndDropCell;
	
	public OnRightClickListener( TreeView<File> treeView, DragAndDropCell dragAndDropCell )
	{
		this.treeView = treeView;
		this.dragAndDropCell = dragAndDropCell;
	}
	
	@Override
	public void handle( MouseEvent event ) 
	{
		if( event.getButton() == MouseButton.SECONDARY )
		{
			TreeItem<File> selectedItem = treeView.getSelectionModel().getSelectedItem();
			if( selectedItem != null )
			{
				dragAndDropCell.setContextMenuFolderPath( selectedItem.getValue().isDirectory() ? 
												   selectedItem.getValue() : selectedItem.getValue().getParentFile() );
			}
			else
				dragAndDropCell.setContextMenuFolderPath( new File( "jython" ) );
		}
	}
}
