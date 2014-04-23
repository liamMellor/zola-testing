package com.cafe.noir.dialogs;

import java.util.Arrays;
import java.util.List;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import com.cafe.noir.buttons.BrowserButton;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.NoirStyleUtilities;

public class SaveDialog 
{
	public enum Response { NO, YES, CANCEL };
	
	public static Response buttonSelected = Response.CANCEL;

	public static List<? extends Object> showConfirmDialog( Stage owner, String message, String title, FrameType ft ) 
	{
	    VBox vb = new VBox();
	    Scene scene = new Scene( vb );
	    
	    final BaseDialog dial = new BaseDialog( title, owner, scene );
	    vb.setPadding( new Insets( 20 , 20, 20, 20 ) );
	    vb.setSpacing( 20 );
	    
	    Button yesButton = new Button( title );
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
	    
	    BrowserButton chromeButton = null;
	    BrowserButton firefoxButton = null;
	    BrowserButton safariButton = null;
	    
	    switch( ft )
	    {
			case Arriere:
			    vb.getChildren().addAll( msg, fileName, bp  );
				break;
			case Avant:
				HBox browserChoice = new HBox();
				chromeButton = new BrowserButton( BrowserButton.BrowserType.CHROME, 50, 50 );
				firefoxButton = new BrowserButton( BrowserButton.BrowserType.FIREFOX, 50, 50 );
				safariButton = new BrowserButton( BrowserButton.BrowserType.SAFARI, 50, 50 );
				
				browserChoice.setAlignment( Pos.CENTER );
				browserChoice.getChildren().addAll( chromeButton, firefoxButton, safariButton );
				
			    vb.getChildren().addAll( msg, title.equals( "Save" ) ? fileName : new HBox(), browserChoice, bp  );
				break;
			case Mobile:
				break;
			default:
			    vb.getChildren().addAll( msg, fileName, bp  );
				break;
	    }

	    NoirStyleUtilities.iPhoneBackgroundStyle( vb );
	    
	    dial.showDialog();
	    
	    return Arrays.asList( buttonSelected, 
	    					  fileName.getText(), 
	    					  ft == FrameType.Avant ? Arrays.asList( chromeButton.getState(), firefoxButton.getState(), safariButton.getState() ) : null );
	}
}