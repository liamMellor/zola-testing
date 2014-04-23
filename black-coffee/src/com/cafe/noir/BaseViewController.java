package com.cafe.noir;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.control.TabPane.TabClosingPolicy;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

import com.cafe.noir.util.density.ScreenSize;

public class BaseViewController extends Application
{
	public static TabPane mainTabbedPane;
	
	public BaseViewController()
	{
		super();
	}
	
	private TabPane initUI() 
    {
        mainTabbedPane = new TabPane();
        
        Tab frontEnd = new Tab( "Front End" );
        frontEnd.setContent( new AvantViewController() );
        
        Tab backEnd = new Tab( "Back End" );
        backEnd.setContent( new ArriereViewController() );
        
        Tab manager = new Tab( "Manager" );
        manager.setContent( new DirecteurViewController() );
        
        mainTabbedPane.getTabs().add( frontEnd );
        mainTabbedPane.getTabs().add( backEnd );
        mainTabbedPane.getTabs().add( manager );

        mainTabbedPane.setTabClosingPolicy( TabClosingPolicy.UNAVAILABLE );
        mainTabbedPane.getStyleClass().add( "special-tab" );
        
        return mainTabbedPane;
    }

	@Override
	public void start( final Stage primaryStage ) throws Exception 
	{
		primaryStage.setTitle( "Black Coffee" );
		primaryStage.setWidth( ScreenSize.getScreenSize().getWidth() );
		primaryStage.setHeight( ScreenSize.getScreenSize().getHeight() );
		Scene scene = new Scene( initUI() );
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