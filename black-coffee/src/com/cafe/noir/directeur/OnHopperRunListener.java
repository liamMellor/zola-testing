package com.cafe.noir.directeur;

import java.io.File;

import javafx.event.EventHandler;
import javafx.scene.control.TreeView;
import javafx.scene.input.MouseEvent;
import javafx.scene.web.WebView;

import com.cafe.noir.util.manager.FileManager;

public class OnHopperRunListener implements EventHandler<MouseEvent>
{
	private WebView webView;
	private TreeView<File> treeView;

	public OnHopperRunListener( WebView webView, TreeView<File> treeView2 )
	{
		this.webView = webView;
		this.treeView = treeView2;
	}
	
	@Override
	public void handle( MouseEvent arg0 ) 
	{
		FileManager.runScript( webView, treeView );
	}
}
