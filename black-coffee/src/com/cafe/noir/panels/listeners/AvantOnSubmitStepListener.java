package com.cafe.noir.panels.listeners;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import com.cafe.noir.avant.BrowserAction;
import com.cafe.noir.avant.OnComboSwitchListener;
import com.cafe.noir.panels.ListPanel;
import com.cafe.noir.util.Toaster;
import com.cafe.noir.util.manager.AvantDataManager;

public class AvantOnSubmitStepListener implements EventHandler<MouseEvent>
{	
	private TextField keysToSend;
	private TextField lineOfHtml;
	private ListPanel listPanel;
	private Button runAllButton;
	private ObservableList<String> listModel;

	public AvantOnSubmitStepListener( TextField keysToSend2, TextField lineOfHtml2, ObservableList<String> observableList, Button button, ListPanel listPanel )
	{
		this.keysToSend = keysToSend2;
		this.lineOfHtml = lineOfHtml2;
		this.listModel = observableList;
		this.runAllButton = button;
		this.listPanel = listPanel;
	}
	
	private void listConstructor( String lineToSend )
	{
		StringBuilder sb = new StringBuilder( 64 );
		sb.append( "Step " + listPanel.getCurrentListNumber() + "\n" );
		sb.append( "Action: " + OnComboSwitchListener.currentAction + "\n" );
		sb.append( "Line to send: " + lineToSend);
		listModel.add( sb.toString() );
	}

	@Override
	public void handle( MouseEvent arg0 ) 
	{
		if( listPanel.getCurrentListNumber() < 1 && OnComboSwitchListener.currentAction != BrowserAction.GoTo )
			Toaster.showDialog( new Stage(), "First step must be a URL!" );
		else
		{
			Map<BrowserAction, String[]> tempMap = new HashMap<BrowserAction, String[]>();
			ArrayList<String> tempList = new ArrayList<String>();
			switch ( OnComboSwitchListener.currentAction )
			{
				case Click:
					listConstructor( lineOfHtml.getText() );
					tempList.add( lineOfHtml.getText() );
					break;
				case EnterText:
					listConstructor( lineOfHtml.getText() + "\nKeys to send: " + keysToSend.getText() );
					tempList.addAll( Arrays.asList( lineOfHtml.getText(), keysToSend.getText() ) );
					break;
				case EnterTextAndSubmit:
					listConstructor( lineOfHtml.getText() + "\nKeys to send and Submit: " + keysToSend.getText() );
					tempList.addAll( Arrays.asList( lineOfHtml.getText(), keysToSend.getText() ) );
					break;
				case GoTo:
					try
					{
						new URL( keysToSend.getText() );
						listConstructor( keysToSend.getText() );
						tempList.add( keysToSend.getText() );
					}
					catch( MalformedURLException e )
					{
						Toaster.showDialog( new Stage(), "Malformed URL!" );
					}
					break;
				default:
					break;
			}
			
			runAllButton.arm();
			listPanel.setCurrentListNumber( listPanel.getCurrentListNumber() + 1 );
	
			String[] finalList = new String[ tempList.size() ];
			tempMap.put( OnComboSwitchListener.currentAction, tempList.toArray( finalList ) );
			AvantDataManager.constructionMap.put( listPanel.getCurrentListNumber(), tempMap );
		}
	}
}
