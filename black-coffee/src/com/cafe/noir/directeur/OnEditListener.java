package com.cafe.noir.directeur;

import java.io.File;

import javafx.event.EventHandler;
import javafx.scene.control.TreeView;
import javafx.scene.input.MouseEvent;

import com.cafe.noir.BaseViewController;
import com.cafe.noir.avant.jython.JythonReader;
import com.cafe.noir.util.FrameType;

public class OnEditListener implements EventHandler<MouseEvent>
{
	private TreeView<File> treeView;

	public OnEditListener( TreeView<File> treeView )
	{
		this.treeView = treeView;
	}
	
	@Override
	public void handle( MouseEvent arg0 ) 
	{
		FrameType ft = new JythonReader( treeView.getSelectionModel().getSelectedItem().getValue() ).getFrameType();
		switch( ft )
		{
			case Arriere:
				BaseViewController.mainTabbedPane.getSelectionModel().select( 1 );
				break;
			case Avant:
				BaseViewController.mainTabbedPane.getSelectionModel().select( 0 );
				break;
			default:
				break;
		}
	}

}
