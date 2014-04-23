package com.cafe.noir.panels.listeners;

import java.io.File;
import java.util.List;

import javafx.concurrent.Task;
import javafx.concurrent.WorkerStateEvent;
import javafx.event.EventHandler;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import com.cafe.noir.avant.jython.JythonCgiGenerator;
import com.cafe.noir.avant.jython.JythonSeleniumGenerator;
import com.cafe.noir.buttons.BrowserButton;
import com.cafe.noir.buttons.BrowserButton.State;
import com.cafe.noir.dialogs.OverwriteDialog;
import com.cafe.noir.dialogs.SaveDialog;
import com.cafe.noir.dialogs.SaveDialog.Response;
import com.cafe.noir.directeur.DirecteurLeftPanel;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.Toaster;
import com.cafe.noir.util.manager.ArriereDataManager;
import com.cafe.noir.util.manager.AvantDataManager;
import com.cafe.noir.util.manager.FileManager;

public class OnSaveAndSubmit implements EventHandler<MouseEvent>
{
	public static final File jythonDir = new File( "jython" );
	private File selSubDir = AvantDataManager.selDir;
	private File cgiSubDir = ArriereDataManager.cgiDir;
	
	private FrameType frameType;
	
	public OnSaveAndSubmit( FrameType ft )
	{
		this.frameType = ft;
	}
	
	@Override
	public void handle( MouseEvent arg0 ) 
	{
		if( !jythonDir.exists() )
			jythonDir.mkdir();
		
		switch ( frameType )
		{
			case Arriere:
				if( !selSubDir.exists() )
					selSubDir.mkdir();
				
				arriereSaveResponse();
				break;
			case Avant:
				if( !cgiSubDir.exists() )
					cgiSubDir.mkdir();
				
				avantSaveResponse();
				break;
			case Mobile:
				break;
			default:
				break;
		}
		
	}
	
	@SuppressWarnings("unchecked")
	private void avantSaveResponse()
	{
		List<? extends Object> response2 = SaveDialog.showConfirmDialog( 
				new Stage(), "Please specify a file name and browser type.", "Save", frameType );
		
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
			{
				Task<Void> showAndWait = Toaster.showDialogAndWait( new Stage(), "Need to select a browser" );
				showAndWait.setOnFailed( new EventHandler<WorkerStateEvent>()
				{
					@Override
					public void handle( WorkerStateEvent arg0 ) 
					{
						avantSaveResponse();
					}
				});
				new Thread( showAndWait ).start();
			}
			else if ( ((String)response2.get( 1 )).equals( "" ) )
			{
				Task<Void> showAndWait = Toaster.showDialogAndWait( new Stage(), "Need to specify a name" );
				showAndWait.setOnFailed( new EventHandler<WorkerStateEvent>()
						{
							@Override
							public void handle( WorkerStateEvent arg0 ) 
							{
								avantSaveResponse();
							}
						});
				new Thread( showAndWait ).start();
			}
			else
			{
				if( FileManager.willOverwrite( selSubDir, ((String)response2.get( 1 )) ) )
				{
					Response response = OverwriteDialog.showConfirmDialog( 
							new Stage(), "A file with that name already exists. Do you wish to overwrite it?", "Yes" );
					switch( response )
					{
					case CANCEL:
						break;
					case NO:
						avantSaveResponse();
						break;
					case YES:
						FileManager.saveFile( selSubDir, ((String)response2.get( 1 )), 
								new JythonSeleniumGenerator( chromeCheck, firefoxCheck, safariCheck, stateCheck ).initJython() );
						DirecteurLeftPanel.notifyDataSetChanged();
						break;
					default:
						break;
					}
				}
				else
				{
					FileManager.saveFile( selSubDir, ((String)response2.get( 1 )), 
							new JythonSeleniumGenerator( chromeCheck, firefoxCheck, safariCheck, stateCheck ).initJython() );
					DirecteurLeftPanel.notifyDataSetChanged();
				}
			}
		}
	}
	
	private void arriereSaveResponse()
	{
		List<? extends Object> response2 = SaveDialog.showConfirmDialog( 
				new Stage(), "Please specify a file name.", "Save", frameType );

		if( ((SaveDialog.Response)response2.get( 0 )) == SaveDialog.Response.YES )
		{
			if( FileManager.willOverwrite( selSubDir, ((String)response2.get( 1 )) ) )
			{
				Response response = OverwriteDialog.showConfirmDialog( 
						new Stage(), "A file with that name already exists. Do you wish to overwrite it?", "Yes" );
				switch( response )
				{
				case CANCEL:
					break;
				case NO:
					avantSaveResponse();
					break;
				case YES:
					FileManager.saveFile( cgiSubDir, ((String)response2.get( 1 )), 
							new JythonCgiGenerator().initJython() );
					DirecteurLeftPanel.notifyDataSetChanged();
					break;
				default:
					break;
				}
			}
			else
			{
				FileManager.saveFile( cgiSubDir, ((String)response2.get( 1 )), 
						new JythonCgiGenerator().initJython() );
				DirecteurLeftPanel.notifyDataSetChanged();
			}
		}
	}
}
