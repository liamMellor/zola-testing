package com.wizard.magus;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

import com.wizard.magus.survey.SurveyWizard;


public class WizardApplicationController extends Application
{
	public WizardApplicationController()
	{
		super();
	}

	@Override
	public void start( final Stage primaryStage ) throws Exception 
	{
		primaryStage.setTitle( "Coffee Wizard" );
		Scene scene = new Scene( new SurveyWizard( primaryStage ), 600, 450 );
		scene.getStylesheets().add( this.getClass().getResource( "/css/styles.css" ).toExternalForm() );

		primaryStage.setScene( scene );
		primaryStage.show();
		primaryStage.setOnCloseRequest( new EventHandler<WindowEvent>()
		{

			@Override
			public void handle( WindowEvent event )
			{
				primaryStage.close();
				Platform.exit();
				System.exit( 0 );
			}
			
		});
	}
	public static void main( String[] args ) 
	{
        launch(args);
	}
}
