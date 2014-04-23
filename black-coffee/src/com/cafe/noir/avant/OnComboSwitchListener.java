package com.cafe.noir.avant;

import java.util.ArrayList;
import java.util.Arrays;

import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.scene.Node;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.Pane;

import com.cafe.noir.util.NoirSwingUtilities;

public class OnComboSwitchListener implements ChangeListener<String>
{	
	private ComboBox<String> actionType;
	private ArrayList<Node> compsComp;
	private ArrayList<Label> labels;

	private TextField keysToSend;

	private Label actionFieldLabel;

	private Label sendKeysFieldLabel;

	private Label lineOfHtmlLabel;

	private Pane vbox;

	private TextField lineOfHtml;
	private AvantLeftPanel alp;
	
	public static BrowserAction currentAction = BrowserAction.GoTo;
	
	public OnComboSwitchListener()
	{
	}
	public OnComboSwitchListener( ComboBox<String> actionType2, 
								  ArrayList<Node> compsComp2, ArrayList<Label> labels2,
								  TextField keysToSend2, Label actionFieldLabel2,
								  Label sendKeysFieldLabel2, Label lineOfHtmlLabel2,
								  Pane vbox,
								  TextField lineOfHtml2, AvantLeftPanel alp ) 
	{
		this.actionType = actionType2;
		this.compsComp = compsComp2;
		this.labels = labels2;
		this.keysToSend = keysToSend2;
		this.actionFieldLabel = actionFieldLabel2;
		this.sendKeysFieldLabel = sendKeysFieldLabel2;
		this.lineOfHtmlLabel = lineOfHtmlLabel2;
		this.vbox = vbox;
		this.lineOfHtml = lineOfHtml2;
		this.alp = alp;
	}

	public void actionPerformed() 
	{
		compsComp.clear();
		labels.clear();
		
		vbox.getChildren().removeAll( vbox.getChildren() );
		vbox.getChildren().clear();
		
		switch( currentAction )
		{
		case Click:
			compsComp.addAll( Arrays.asList( actionType, lineOfHtml ) );
			labels.addAll( Arrays.asList( actionFieldLabel,  lineOfHtmlLabel ) );
			
		    NoirSwingUtilities.addLabelTextRowsComps( labels, compsComp, vbox );		
			break;
		case EnterText:
		case EnterTextAndSubmit:
			compsComp.addAll( Arrays.asList( actionType, keysToSend, lineOfHtml ) );
			labels.addAll( Arrays.asList( actionFieldLabel, sendKeysFieldLabel,  lineOfHtmlLabel ) );
			
			sendKeysFieldLabel.setText( "Text: " );
			
		    NoirSwingUtilities.addLabelTextRowsComps( labels, compsComp, vbox );
			break;
		case GoTo:
			compsComp.addAll( Arrays.asList( actionType, keysToSend ) );
			labels.addAll( Arrays.asList( actionFieldLabel,  sendKeysFieldLabel ) );
			
			sendKeysFieldLabel.setText( "URL: " );

		    NoirSwingUtilities.addLabelTextRowsComps( labels, compsComp, vbox );
			break;
		default:
			break;
		}
		vbox.getChildren().add( alp.mSubmit );
	}
	@Override
	public void changed( ObservableValue<? extends String> observable, String oldValue, String newValue ) 
	{
		if ( newValue.equals( "Go To" ) )
			currentAction = BrowserAction.GoTo;
		else if ( newValue.equals( "Click" ) )
			currentAction = BrowserAction.Click;
		else if ( newValue.equals( "Enter Text" ) )
			currentAction = BrowserAction.EnterText;
		else if ( newValue.equals( "Enter Text and Submit" ) )
			currentAction = BrowserAction.EnterTextAndSubmit;	
		
		actionPerformed();
	}
}
