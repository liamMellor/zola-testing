package com.cafe.noir.panels.listeners;

import java.util.List;

import javafx.event.EventHandler;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import com.cafe.noir.ArriereViewController;
import com.cafe.noir.AvantViewController;
import com.cafe.noir.arriere.ArriereLeftPanel;
import com.cafe.noir.avant.AvantLeftPanel;
import com.cafe.noir.avant.jython.JythonCgiGenerator;
import com.cafe.noir.avant.jython.JythonSeleniumGenerator;
import com.cafe.noir.buttons.BrowserButton;
import com.cafe.noir.buttons.BrowserButton.State;
import com.cafe.noir.dialogs.SaveDialog;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.Toaster;
import com.cafe.noir.util.manager.FileManager;

public class OnRunListener implements EventHandler<MouseEvent>
{
	public static final String PYTHON = new String( "python" );
	public static final String TEMP_SEL_FILE = new String( "jython/temp_sel.py" );
	public static final String TEMP_CGI_FILE = new String( "jython/temp_cgi.py" );

	private FrameType ft;
	
	public OnRunListener( FrameType ft )
	{
		this.ft = ft;
	}
	
	@SuppressWarnings("unchecked")
	@Override
	public void handle( MouseEvent arg0 ) 
	{
		switch ( ft )
		{
			case Arriere:
				if ( ArriereLeftPanel.listPanel.getListModel().size() > 0 )
				{
					FileManager.saveTempScriptAndRun( ArriereViewController.tabPane, 
							   ArriereViewController.terminal, 
							   TEMP_CGI_FILE, 
							   new JythonCgiGenerator().initJython() );
				}
				break;
			case Avant:
				if( AvantLeftPanel.listPanel.getListModel().size() > 0 )
				{
					List<? extends Object> response2 = SaveDialog.showConfirmDialog( 
							new Stage(), "Select one or more browsers", "Run", FrameType.Avant );
	
					boolean chromeCheck = false;
					boolean firefoxCheck = false;
					boolean safariCheck = false;
					
					int stateCheck = 0;
	
					if( ((SaveDialog.Response)response2.get( 0 )) == SaveDialog.Response.YES )
					{
						int i = 0;
						for( State state : ((List<BrowserButton.State>)response2.get( 2 )) )
						{
							if( state == BrowserButton.State.ACTIVE )
							{
								stateCheck++;
								switch( i )
								{
								case 0:
									chromeCheck = true;
									break;
								case 1:
									firefoxCheck = true;
									break;
								case 2:
									safariCheck = true;
									break;
								}
							}
							i++;
						}
						if( stateCheck == 0 )
							Toaster.showDialog( new Stage(), "Need to select a browser" );
					}
					FileManager.saveTempScriptAndRun( AvantViewController.tabPane, 
							   AvantViewController.terminal, 
							   TEMP_SEL_FILE, 
							   new JythonSeleniumGenerator( chromeCheck, firefoxCheck, safariCheck, stateCheck ).initJython() );
				}
				break;
			case Mobile:
				break;
			default:
				break;
		}
	}
}
