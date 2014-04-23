package com.cafe.noir.util;

import javafx.concurrent.Task;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

public class Toaster
{	
	static class Dialog extends Stage 
	{
	    public Dialog( String title, Stage owner, Scene scene ) 
	    {
	    	initStyle( StageStyle.UNDECORATED );
	        initModality( Modality.WINDOW_MODAL );
	        initOwner( owner );
			scene.getStylesheets().add( this.getClass().getResource( "/css/styles.css" ).toExternalForm() );
	        setScene( scene );
	    }
	    public void showDialog() 
	    {
	        sizeToScene();
	        centerOnScreen();
	        show();
	    }
	    public void showDialogAndWait() 
	    {
	        sizeToScene();
	        centerOnScreen();
	        showAndWait();
	    }
	}

	static class Message extends Text 
	{
	    public Message( String msg ) 
	    {
	        super( msg );
	        setWrappingWidth( 250 );
	        setFill( Color.WHITE );
	    }
	}
	
	private static Dialog dialSetup( Stage owner, String toast )
	{
		VBox vb = new VBox();
	    
	    vb.setPadding( new Insets( 20, 20, 20, 20 ) );
	    
	    HBox msg = new HBox();
	    
	    msg.getChildren().addAll( new Message( toast ) );
	    msg.setAlignment( Pos.CENTER );
	    
	    vb.getChildren().add( msg );
	    vb.setAlignment( Pos.CENTER );
	    
	    NoirStyleUtilities.warningBackgroundStyle( vb );
	    
	    Scene scene = new Scene( vb );
	    
	    final Dialog dial = new Dialog( "Error", owner, scene );
	    dial.setOpacity( 0 );
	    return dial;
	}
	
    public static void showDialog( Stage owner, String toast ) 
    {
    	Dialog dial = dialSetup( owner, toast );

	    dial.showDialog();

        new Thread( new FadeAnim( dial ) ).start();
    }
    
    public static Task<Void> showDialogAndWait( Stage owner, String toast ) 
    {
    	Dialog dial = dialSetup( owner, toast );

    	dial.showDialog();
    	
    	Task<Void> task = new FadeAnim( dial );
        return task;
    }
}