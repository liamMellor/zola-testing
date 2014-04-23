package com.cafe.noir.panels.listeners;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import com.cafe.noir.panels.ListPanel;
import com.cafe.noir.util.manager.ArriereDataManager;

public class ArriereOnSubmitStepListener implements EventHandler<MouseEvent>
{	
	private ListPanel listPanel;
	private Button runAllButton;
	private ObservableList<String> listModel;
	private VBox vbox;

	public ArriereOnSubmitStepListener( VBox vbox, ObservableList<String> observableList, Button button, ListPanel listPanel )
	{
		this.vbox = vbox;
		this.listModel = observableList;
		this.runAllButton = button;
		this.listPanel = listPanel;
	}
	private void listConstructor( String kvp, String url )
	{
		StringBuilder sb = new StringBuilder( 64 );
		sb.append( "Step " + listPanel.getCurrentListNumber() + "\n" );
		sb.append( "URL: " + url + "\n" );
		sb.append( "KeyValuePairs: " + kvp );
		listModel.add( sb.toString() );
	}

	@Override
	public void handle( MouseEvent arg0 ) 
	{
		runAllButton.arm();
		listPanel.setCurrentListNumber( listPanel.getCurrentListNumber() + 1 );
		Map<String, String> tempMap = new HashMap<String, String>();
		
		String key = null;
		String value = null;
		String url = null;
		for( Node vChilds : vbox.getChildren() )
		{
			if( vChilds instanceof HBox )
			{
				for( Node node : ((HBox) vChilds).getChildren() )
					if( node instanceof TextField )
						if( node.getId().equals( "KEY" ) )
							key = ((TextField)node).getText();
						else if( node.getId().equals( "VALUE" ) )
							value = ((TextField)node).getText();
			}
			else if ( vChilds instanceof TextField )
				if( vChilds.getId().equals( "URL" ) )
					url = ((TextField)vChilds).getText();
			if( key != null && value != null )
			{
				tempMap.put( key, value );
				key = null;
				value = null;
			}			
		}
		StringBuilder sb = new StringBuilder( 64 );
		for( Entry<String, String> entries : tempMap.entrySet() )
		{
			sb.append( "\n     " + entries.getKey() + ", " + entries.getValue() );
		}
		listConstructor( sb.toString(), url );
		
		Map<String, Map<String,String>> innerMap = new HashMap<String, Map<String,String>>();
		innerMap.put( url, tempMap );
		ArriereDataManager.constructionMap.put( listPanel.getCurrentListNumber(), innerMap );
	}
}