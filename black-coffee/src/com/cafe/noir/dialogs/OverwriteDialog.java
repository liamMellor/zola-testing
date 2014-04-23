package com.cafe.noir.dialogs;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import com.cafe.noir.dialogs.SaveDialog.Response;
import com.cafe.noir.util.NoirStyleUtilities;

public class OverwriteDialog 
{
    private static Response buttonSelected;

	public static Response showConfirmDialog( Stage owner, String message, String title ) 
	{
	    VBox vb = new VBox();
	    Scene scene = new Scene( vb );
	    
	    final BaseDialog dial = new BaseDialog( title, owner, scene );
	    vb.setPadding( new Insets( 20 , 20, 20, 20 ) );
	    vb.setSpacing( 20 );
	    
	    Button yesButton = new Button( "Yes" );
	    yesButton.setOnAction( new EventHandler<ActionEvent>() 
		{
			@Override 
	        public void handle( ActionEvent e ) 
	        {
	            dial.close();
	            buttonSelected = Response.YES;
	        }
	    });
	    
	    Button noButton = new Button( "Cancel" );
	    noButton.setOnAction( new EventHandler<ActionEvent>() 
		{
	        @Override 
	        public void handle( ActionEvent e ) 
	        {
	            dial.close();
	            buttonSelected = Response.NO;
	        }
	    });
	    
	    NoirStyleUtilities.iPhoneButtonStyle( yesButton, noButton );
	    
	    BorderPane bp = new BorderPane();
	    HBox buttons = new HBox();
	    
	    buttons.setAlignment( Pos.CENTER );
	    buttons.setSpacing( 20 );
	    buttons.getChildren().addAll( yesButton, noButton );
	    bp.setCenter( buttons );
	    	    
	    HBox msg = new HBox();
	    msg.setSpacing( 20 );
	    msg.getChildren().addAll( new Message( message ) );
	    
	    vb.getChildren().addAll( msg, buttons );
	    
	    NoirStyleUtilities.iPhoneBackgroundStyle( vb );
	    
	    dial.showAndWait();
	    
	    return buttonSelected;
	}
}
