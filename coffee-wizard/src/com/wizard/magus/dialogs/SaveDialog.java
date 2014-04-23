package com.wizard.magus.dialogs;

import java.util.Arrays;
import java.util.List;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import com.wizard.magus.util.NoirStyleUtilities;

public class SaveDialog 
{
	public enum Response { YES, CANCEL };
	
	public static Response buttonSelected = Response.CANCEL;

	public static List<? extends Object> showConfirmDialog( Stage owner, String message, String title  ) 
	{
	    VBox vb = new VBox();
	    Scene scene = new Scene( vb );
	    
	    final BaseDialog dial = new BaseDialog( title, owner, scene );
	    vb.setPadding( new Insets( 20 , 20, 20, 20 ) );
	    vb.setSpacing( 20 );
	    
	    Button yesButton = new Button( "Install" );
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
	            buttonSelected = Response.CANCEL;
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
	    
	    TextField fileName = new TextField();
	    Label l = new Label( "Password:" );
	    l.setLabelFor( fileName );
	    
	    vb.getChildren().addAll( msg, l, fileName, bp  );
			

	    NoirStyleUtilities.iPhoneBackgroundStyle( vb );
	    
	    dial.showDialog();
	    
	    return Arrays.asList( buttonSelected, 
	    					  fileName.getText() );
	}
}