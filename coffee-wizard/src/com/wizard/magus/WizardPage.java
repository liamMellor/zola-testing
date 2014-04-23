package com.wizard.magus;

import java.util.List;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.control.ContentDisplay;
import javafx.scene.control.Label;
import javafx.scene.control.LabelBuilder;
import javafx.scene.control.ProgressBar;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Priority;
import javafx.scene.layout.Region;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import com.wizard.magus.dialogs.SaveDialog;
import com.wizard.magus.dialogs.SaveDialog.Response;
import com.wizard.magus.util.FileManager;
import com.wizard.magus.util.Make;
import com.wizard.magus.util.NoirStyleUtilities;

public abstract class WizardPage extends VBox 
{
	protected Button priorButton   = new Button("_Previous");
	protected Button nextButton    = new Button("N_ext");
	protected Button cancelButton  = new Button("Cancel");
	protected Button finishButton  = new Button("_Finish");
	protected Image activeIcn = new Image( "/img/active_icn.png", 15, 15, false, true );
	protected Image inactiveIcn =new Image( "/img/inactive_icn.png", 15, 15, false, true );
	protected String[] nav = 
		{ 
			"Introduction", 
			"Read Me", 
			"Destination Select", 
			"Installation", 
			"Summary" 
		};
	protected Label[] labs = 
		{ 
			new Label( nav[0], new ImageView( inactiveIcn ) ),
			new Label( nav[1], new ImageView( inactiveIcn ) ),
			new Label( nav[2], new ImageView( inactiveIcn ) ), 
			new Label( nav[3], new ImageView( inactiveIcn ) ), 
			new Label( nav[4], new ImageView( inactiveIcn ) ), 
		};
	private Label progLabel;
	
	protected WizardPage( String title ) 
	{
		setLabsInactive();
		
		Label topTitle = LabelBuilder.create().text(title).style("-fx-font-weight: bold; -fx-padding: 0 0 5 0;").build();
		topTitle.setAlignment( Pos.CENTER );
		getChildren().add( topTitle );
		setAlignment( Pos.CENTER );
		setId(title);
		setSpacing( 10 );
		getStyleClass().add( "iphone-toolbar" );
	 
		Region spring = new Region();
		HBox.setHgrow( spring, Priority.ALWAYS );
		VBox.setVgrow( spring, Priority.ALWAYS );
		
		HBox hbox = new HBox();
		
		StackPane pane = new StackPane();
		
		pane.getStyleClass().add( "stackpane" );
		
		pane.setPrefWidth( 400 );
		pane.setPrefHeight( 500 );
		pane.setAlignment( Pos.TOP_LEFT );
		pane.getChildren().addAll( getContent() );
		
		hbox.setSpacing( 50 );
		
		hbox.getChildren().addAll( leftLights(), pane );
		getChildren().addAll( hbox, spring, getButtons() );
	 
		priorButton.setOnAction( new EventHandler<ActionEvent>() 
		{
			@Override
			public void handle( ActionEvent actionEvent ) 
			{
				priorPage();
			}
		});
		nextButton.setOnAction( new EventHandler<ActionEvent>() 
		{
			@Override
			public void handle( ActionEvent actionEvent )
			{
				nextPage();
			}
		});
		cancelButton.setOnAction(new EventHandler<ActionEvent>() 
	    {
			@Override
			public void handle( ActionEvent actionEvent ) 
			{
				getWizard().cancel();
			}
	    });
		finishButton.setOnAction(new EventHandler<ActionEvent>() 
		{
			@Override
			public void handle(ActionEvent actionEvent) 
			{
				getWizard().finish();
			}
		});
	  }
	 
	  HBox getButtons() 
	  {
		  Region spring = new Region();
		  HBox.setHgrow( spring, Priority.ALWAYS );
		  HBox buttonBar = new HBox(5);
		  cancelButton.setCancelButton( true );
		  finishButton.setDefaultButton( true );
		  NoirStyleUtilities.iPhoneButtonStyle( priorButton, nextButton, cancelButton, finishButton );
		  buttonBar.getChildren().addAll( spring, priorButton, nextButton, cancelButton, finishButton );
		  return buttonBar;
	  }
	  
	  VBox leftLights()
	  {
		  VBox vbox = new VBox();
		  vbox.setSpacing( 5 );
		  vbox.setPadding( new Insets( 40, 0, 0, 0 ) );
		  for( Label lab : labs )
		  {
			  lab.getStyleClass().add( "label-spec" );
			  lab.setGraphicTextGap( 5 );
			  lab.setContentDisplay(ContentDisplay.LEFT);
			  vbox.getChildren().add( lab );
		  }
		  return vbox;
	  }
	  
	  protected abstract Parent getContent();
	 
	  boolean hasNextPage() 
	  {
	    return getWizard().hasNextPage();
	  }
	 
	  boolean hasPriorPage() 
	  {
	    return getWizard().hasPriorPage();
	  }
	 
	  protected void nextPage() 
	  {
	    getWizard().nextPage();
	  }
	 
	  void priorPage() 
	  {
	    getWizard().priorPage();
	  }
	  
	  protected void navTo( String id ) 
	  {
	    getWizard().navTo(id);
	  }
	 
	  public void navSpecial()
	  {
	    	List<? extends Object> resp = SaveDialog.showConfirmDialog( new Stage(), "Installer is trying to install new software.\nType your password to allow this.", "" );
		    switch ( ((Response)resp.get(0)) )
		    {
			  	case CANCEL:
			  		progLabel.setText( "Installation failed." );
					progLabel.setGraphic( new ImageView( new Image( getClass().getResourceAsStream( "/img/failure_icn.png" ), 50, 50, true, true ) ) );
					priorButton.setDisable( true );
					break;
				case YES:
					FileManager.sudo = ((String)resp.get(1));
					new Thread( new Make( progBar ) ).start();
					break;
				default:
					break;
		    }
	  }
	  
	  private ProgressBar progBar;
	  
	  Wizard getWizard() 
	  {
	    return (Wizard) getParent();
	  }
	  public void setProgLabel( Label pBar )
	  {
		  progLabel = pBar;
	  }
	  public void setProgbar( ProgressBar pBar )
	  {
		  progBar = pBar;
	  }
	  public void manageButtons() 
	  {
	    if (!hasPriorPage()) 
	    {
	      priorButton.setDisable(true);
	    }
	 
	    if (!hasNextPage()) 
	    {
	      nextButton.setDisable(true);
	    }
	  }
	  public void setLabsInactive()
	  {
		  for( Label lab : labs )
		  {
			  lab.setGraphic( new ImageView( inactiveIcn ) );
		  }
	  }
}