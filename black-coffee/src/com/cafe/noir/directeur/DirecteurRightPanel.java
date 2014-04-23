package com.cafe.noir.directeur;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.web.WebView;

import com.cafe.noir.util.NoirStyleUtilities;

public class DirecteurRightPanel extends BorderPane
{
	private WebView terminal;

	public DirecteurRightPanel()
	{
		super();
		setCenter( terminalPanel() );
		setBottom( buttonPane() );
	}
	
	public ScrollPane terminalPanel()
	{
		terminal = new WebView();
		terminal.setPrefWidth( 500 );
		
		ScrollPane terminalScroll = new ScrollPane();
		
		terminalScroll.setContent( terminal );
		terminalScroll.setFitToHeight( true );
		terminalScroll.setFitToWidth( true );
		terminalScroll.setPrefWidth( 500 );
		
		return terminalScroll;
	}
	
	public WebView getTerminal()
	{
		return terminal;
	}
	
	private HBox buttonPane()
    {      
    	Button resetButton = new Button( "Clear" );
        
        NoirStyleUtilities.iPhoneButtonStyle( resetButton );
        
    	HBox buttonPane = new HBox();
        buttonPane.setPadding( new Insets( 15, 12, 15, 12 ) );
    	buttonPane.setSpacing( 60 );
        buttonPane.setAlignment( Pos.CENTER );
                
        buttonPane.getChildren().add( resetButton );
                
        return buttonPane;
    }
}
