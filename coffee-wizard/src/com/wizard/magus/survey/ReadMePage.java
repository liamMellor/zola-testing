package com.wizard.magus.survey;

import java.io.IOException;

import javafx.scene.Parent;
import javafx.scene.image.ImageView;
import javafx.scene.web.WebView;

import com.wizard.magus.WizardPage;
import com.wizard.magus.util.FileManager;

public class ReadMePage extends WizardPage 
{	 
	  public ReadMePage() 
	  {
	    super( "Important Information" );
	    
	    labs[1].setGraphic( new ImageView( activeIcn ) );
	    
	    nextButton.setDisable( false );
	    finishButton.setDisable( true );
	  }
	  
	  protected Parent getContent() 
	  {
		  WebView webView = new WebView();
		  
		  try 
		  {
			  webView.getEngine().loadContent( FileManager.inputStreamToString( getClass().getResourceAsStream( "/html/readme.html" ) ) );
		  } 
		  catch ( IOException e )
		  {
			  e.printStackTrace();
		  }
		  webView.setPrefWidth( 400 );
		  webView.setPrefHeight( 500 );
		  return webView;
	  }
	 
	  protected void nextPage() 
	  {
		  super.nextPage();
	  }
}