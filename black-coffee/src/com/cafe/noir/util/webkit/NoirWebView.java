package com.cafe.noir.util.webkit;

import java.net.MalformedURLException;
import java.net.URL;

import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;

import com.cafe.noir.util.NoirStyleUtilities;
import com.cafe.noir.util.density.ScreenSize;

public class NoirWebView 
{
    private WebEngine engine;

    private Label lblStatus = new Label();

    private Button btnGo = new Button( "Go" );
    private TextField txtURL = new TextField();
    private ProgressBar progressBar = new ProgressBar();
    private String url;
    
    public NoirWebView( String url )
    {
    	this.url = url;
    }
    public VBox initComponents() 
    {
        VBox borderPane = new VBox();
        
        HBox hbox = new HBox();
        hbox.setPadding( new Insets( 15, 12, 15, 12 ) );
        hbox.setSpacing( 10 );
        
        NoirStyleUtilities.iPhoneBackgroundStyle( hbox );
        NoirStyleUtilities.iPhoneButtonStyle( btnGo );
        
        EventHandler<MouseEvent> al = new EventHandler<MouseEvent>() 
        {
			@Override
			public void handle( MouseEvent arg0 ) 
			{
                loadURL( txtURL.getText() );
			}
        };
        
        btnGo.setOnMouseClicked( al );
        
        txtURL.setMinWidth( 500 );
        txtURL.setPrefWidth( 500 );
        
        hbox.getChildren().add( txtURL );
        hbox.getChildren().add( btnGo );
        hbox.setAlignment( Pos.CENTER );
        
        WebView webView = createScene();
        
        ScrollPane scroll = new ScrollPane();
        scroll.setContent( webView );

        scroll.setFitToWidth( true );
        scroll.setPrefHeight( 525 );
        
        progressBar.setPrefWidth( 700 );
        
        borderPane.getChildren().addAll( hbox, scroll, progressBar );
        
        scroll.setFitToHeight( true );
        
		return borderPane;
    }
    
    public WebView createScene() 
    {
        final WebView view = new WebView();

        engine = view.getEngine();
        
		Engine eng = new Engine( engine, lblStatus, txtURL );
        
        progressBar.progressProperty().bind( engine.getLoadWorker().progressProperty() );
        
        view.setMaxHeight( ScreenSize.getScreenSize().getHeight() * 0.75 );
        
        view.setOnZoom( new OnZoomListener( eng ) );
        return view;
    }

    public void loadURL( final String url ) 
    {
        String tmp = toURL(url);

        if (tmp == null) {
            tmp = toURL( "http://" + url );
        }

        engine.load( tmp );
    }

    private static String toURL(String str) 
    {
        try 
        {
            return new URL(str).toExternalForm();
        } 
        catch ( MalformedURLException exception ) 
        {
            return null;
        }
    }
    
    public Pane create() 
    {
        final NoirWebView noirWebView = new NoirWebView( url );
    	Pane webPagePane = noirWebView.initComponents();
    	
        noirWebView.loadURL( url );
        
        return webPagePane;
    }
}