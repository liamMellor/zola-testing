package com.cafe.noir.panels;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.web.WebView;

import com.cafe.noir.panels.listeners.OnResetListener;
import com.cafe.noir.panels.listeners.OnSaveAndSubmit;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.NoirStyleUtilities;

public class TerminalPanel extends BorderPane
{
	private WebView terminal;
	private FrameType frameType;

	public TerminalPanel( FrameType ft )
	{
		super();
		this.frameType = ft;
		
		terminal = new WebView();
		ScrollPane terminalScroll = new ScrollPane();
		terminalScroll.setContent( terminal );
		terminalScroll.setFitToHeight( true );
		terminalScroll.setFitToWidth( true );
		
		setCenter( terminalScroll );
		setBottom( buttonPane() );
	}
	
	public WebView getTerminal()
	{
		return terminal;
	}
	
	private HBox buttonPane()
    {      
    	Button resetButton = new Button( "Reset" );
    	Button saveButton = new Button( "Save and Submit" );
        
    	resetButton.setOnMouseClicked( new OnResetListener( frameType ) );
    	saveButton.setOnMouseClicked( new OnSaveAndSubmit( frameType ) );
        NoirStyleUtilities.iPhoneButtonStyle( resetButton, saveButton );
        
    	HBox buttonPane = new HBox();
        buttonPane.setPadding( new Insets( 15, 12, 15, 12 ) );
    	buttonPane.setSpacing( 60 );
        buttonPane.setAlignment( Pos.CENTER );
        
    	NoirStyleUtilities.iPhoneBackgroundStyle( buttonPane );
        
        buttonPane.getChildren().add( resetButton );
        buttonPane.getChildren().add( saveButton );
                
        return buttonPane;
    }
}
