package com.cafe.noir.util.webkit;

import static javafx.concurrent.Worker.State.FAILED;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebEvent;
import javafx.stage.Stage;

import javax.swing.JOptionPane;

import org.w3c.dom.Document;

import com.cafe.noir.util.Toaster;

public class Engine
{
	private WebEngine engine;

	public Engine( final WebEngine engine, final Label lblStatus, final TextField txtURL )
	{	
		this.engine = engine;
		engine.titleProperty().addListener(new ChangeListener<String>() 
		{
            @Override
            public void changed(ObservableValue<? extends String> observable, String oldValue, final String newValue) 
            {
            }
        });
        engine.documentProperty().addListener(new ChangeListener<Document>() 
		{
            @Override public void changed( ObservableValue<? extends Document> prop, Document oldDoc, Document newDoc ) 
            {
            	initZoomOut( engine );
            	enableFirebug( engine );
            }
		});
        engine.setOnStatusChanged( new EventHandler<WebEvent<String>>()
		{
            @Override public void handle( final WebEvent<String> event )
            {
                lblStatus.setText( event.getData() );
            }
        });

	    engine.locationProperty().addListener(new ChangeListener<String>()
		{
	        @Override
	        public void changed(ObservableValue<? extends String> ov, String oldValue, final String newValue) 
	        {
	            txtURL.setText(newValue);
	        }
	    });
	
	    engine.getLoadWorker()
	            .exceptionProperty()
	            .addListener(new ChangeListener<Throwable>() 
	    		{
	            	@Override
	                public void changed(ObservableValue<? extends Throwable> o, Throwable old, final Throwable value) 
	            	{
	                    if (engine.getLoadWorker().getState() == FAILED) 
	                    {
	                            Toaster.showDialog( new Stage(), (value != null) ? engine.getLocation() + "\n" + value.getMessage() :
	                                    engine.getLocation() + "\nUnexpected error." +
	                                    "Loading error..." + JOptionPane.ERROR_MESSAGE );
	                    }
	                }
	            });
	}
	
	/**
     * Enables Firebug Lite for debugging a webEngine.
     * @param engine the webEngine for which debugging is to be enabled.
     */
    private void enableFirebug( final WebEngine engine ) 
    {
    	engine.executeScript("if (!document.getElementById('FirebugLite')){E = document['createElement' + 'NS'] && document.documentElement.namespaceURI;E = E ? document['createElement' + 'NS'](E, 'script') : document['createElement']('script');E['setAttribute']('id', 'FirebugLite');E['setAttribute']('src', 'https://getfirebug.com/' + 'firebug-lite.js' + '#startOpened');E['setAttribute']('FirebugLite', '4');(document['getElementsByTagName']('head')[0] || document['getElementsByTagName']('body')[0]).appendChild(E);E = new Image;E['setAttribute']('src', 'https://getfirebug.com/' + '#startOpened');}"); 
    }
    private void initZoomOut( final WebEngine engine ) 
    {
    	engine.executeScript( "document.body.style.zoom=0.5;this.blur();" );
    }
    
    public void setZoom( double zoomFactor )
    {
    	engine.executeScript( "document.body.style.zoom=" + zoomFactor + ";this.blur();" );
    }
}
