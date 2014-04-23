package com.cafe.noir.directeur;

import java.io.File;
import java.util.ArrayList;

import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;
import javafx.stage.Stage;

import com.cafe.noir.dialogs.OverwriteDialog;
import com.cafe.noir.dialogs.SaveDialog.Response;
import com.cafe.noir.util.Toaster;
import com.cafe.noir.util.manager.FileManager;

public class OnDeleteListener implements EventHandler<ActionEvent>
{
	private TreeView<File> treeView;

	public OnDeleteListener( TreeView<File> treeView ) 
	{
		this.treeView = treeView;
	}

	@Override
	public void handle( ActionEvent event ) 
	{
		ObservableList<TreeItem<File>> items = treeView.getSelectionModel().getSelectedItems();
		
		StringBuilder sb = new StringBuilder();
		ArrayList<File> fileList = new ArrayList<File>();
		sb.append( "Are you sure you wish to remove the following files?\n" );
		for( TreeItem<File> item : items )
		{
			fileList.add( item.getValue() );
			sb.append( "   - " + item.getValue().getName() + "\n" );
		}
		Response resp = OverwriteDialog.showConfirmDialog( new Stage(), sb.toString(), "Delete Files" );
		if( resp == Response.YES )
		{
			File[] fileArr = new File[ fileList.size() ];
			ArrayList<Boolean> boolList = FileManager.deleteFiles( new ArrayList<Boolean>(), fileList.toArray( fileArr ) );
			int successfulDeletions = 0;
			int failedDeletions = 0;
			for( boolean bool : boolList )
			{
				if( bool ) successfulDeletions++;
				else failedDeletions++;
			}
			sb = new StringBuilder();
			
			sb.append( "Successfully deleted " + successfulDeletions + " files." );
			if( failedDeletions > 0 ) sb.append( "\nFailed to delete " + failedDeletions + " files." );
			
			Toaster.showDialog( new Stage(), sb.toString() );
			DirecteurLeftPanel.notifyDataSetChanged();
		}
	}
}
