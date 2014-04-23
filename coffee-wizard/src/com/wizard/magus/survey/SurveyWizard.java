package com.wizard.magus.survey;

import javafx.scene.Parent;
import javafx.scene.control.Label;
import javafx.scene.layout.Priority;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.StackPaneBuilder;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import com.wizard.magus.Wizard;
import com.wizard.magus.WizardPage;

public class SurveyWizard extends Wizard 
{
	  Stage owner;
	  public SurveyWizard( Stage owner ) 
	  {
	    super( new IntroPage(), new ReadMePage(), new DestinationSelectPage(), new InstallationPage(), new ThanksPage() );
	    this.owner = owner;
	  }
	  public void finish()
	  {
	    owner.close();
	  }
	  public void cancel()
	  {
	    System.out.println("Cancelled");
	    owner.close();
	  }
	}
		 
	class ThanksPage extends WizardPage 
	{
	  public ThanksPage() 
	  {
	    super( "Thanks" );
	  }
	 
	  protected Parent getContent() 
	  {
	    StackPane stack = StackPaneBuilder.create().children(
	        new Label("Thanks!")
	    ).build();
	    VBox.setVgrow(stack, Priority.ALWAYS);
	    return stack;
	  }
	}
