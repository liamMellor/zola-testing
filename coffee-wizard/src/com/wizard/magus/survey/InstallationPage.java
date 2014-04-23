package com.wizard.magus.survey;

import javafx.scene.Parent;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;

import com.wizard.magus.WizardPage;

public class InstallationPage extends WizardPage 
{	 
	private Label progLabel;
	private ProgressBar pBar;

	public InstallationPage() 
	  {
	    super( "Important Information" );
	    
	    labs[3].setGraphic( new ImageView( activeIcn ) );
	    
	    nextButton.setDisable( true );
	    priorButton.setDisable( true );
	    finishButton.setDisable( true );
	  }
	  
	  protected Parent getContent() 
	  {
		  progLabel = new Label( "Preparing for installation" );
		  setProgLabel( progLabel );
		  
		  pBar = new ProgressBar();
		  setProgbar( pBar );
		  pBar.setPrefWidth( 500 );
		  
		  VBox vbox = new VBox();
		  vbox.getChildren().addAll( progLabel, pBar );
		  
		  return vbox;
	  }
}
