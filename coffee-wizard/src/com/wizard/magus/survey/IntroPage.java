package com.wizard.magus.survey;

import javafx.scene.Parent;
import javafx.scene.image.ImageView;
import javafx.scene.web.WebView;

import com.wizard.magus.WizardPage;

public class IntroPage extends WizardPage 
{	 
	  public IntroPage() 
	  {
	    super( "Welcome to the Black Coffee Installer" );
	    
	    labs[0].setGraphic( new ImageView( activeIcn ) );
	    
	    nextButton.setDisable( false );
	    finishButton.setDisable( true );
	  }
	  
	  protected Parent getContent() 
	  {
		  WebView webView = new WebView();
		  
		  String text = new String( "<body><p style='width:100%;font-family:Arial;font-size:12px;'><b>Welcome to the Black Coffee for Mac OS X Installer</b></br>"
			  		+ "Black Coffee provides the infrastructure that allows easy creation of "
			  		+ "front end and back end testing on Mac OS X 10.9 systems.</br>"
			  		+ "</br><a href='http://bookish.com'>http://www.bookish.com/</a></br>"
			  		+ "</br>This installer guides you through the steps necessary to install Black Coffee 1.0.0 for Mac OS X. "
			  		+ "</br>To get started, click Continue.</p></body>");
		  
		  webView.getEngine().loadContent( text );
		  webView.setPrefWidth( 400 );
		  webView.setPrefHeight( 500 );
		  return webView;
	  }
	 
	  protected void nextPage() 
	  {
	    // If they have complaints, go to the normal next page
	    super.nextPage();
	  }
	}