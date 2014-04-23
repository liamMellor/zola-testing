package com.cafe.noir.avant;

import java.util.ArrayList;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import com.cafe.noir.panels.ListPanel;
import com.cafe.noir.panels.listeners.AvantOnSubmitStepListener;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.NoirStyleUtilities;
import com.cafe.noir.util.NoirSwingUtilities;

public class AvantLeftPanel extends BorderPane
{
	private ComboBox<String> actionType;
	private TextField keysToSend;
	private TextField lineOfHtml;
	
	private ArrayList<ComboBox<?>> comboBoxes = new ArrayList<ComboBox<?>>();
	private ArrayList<TextField> textFields = new ArrayList<TextField>();
	private ArrayList<Label> labels = new ArrayList<Label>();
	
	private Label actionFieldLabel;
	private Label sendKeysFieldLabel;
	private Label lineOfHtmlLabel;

	private ArrayList<Node> compsComp;
	public Button mSubmit;
	public static ListPanel listPanel;

    protected static final String actionString = "Action";
    protected static final String sendKeysString = "URL";
    
	public AvantLeftPanel()
	{
		super();

		ObservableList<String> actions = FXCollections.observableArrayList( 
				"Go To" , "Click", "Enter Text", "Enter Text and Submit" );
		
		actionType = new ComboBox<String>(actions);
		actionType.setId( actionString );
		actionType.getStyleClass().add( "combo-box-base" );
		ObservableList<Node> nodes = actionType.getChildrenUnmodifiable();
		for ( Node node : nodes )
			node.getStyleClass().add( "combo-box-base list-cell" );
		
		keysToSend = new TextField();
		keysToSend.setId( sendKeysString );
	     
		actionFieldLabel = new Label( actionString + ": " );
		actionFieldLabel.setLabelFor( actionType );
		
		sendKeysFieldLabel = new Label( sendKeysString + ": " );
		sendKeysFieldLabel.setLabelFor( keysToSend );

		lineOfHtml = new TextField();
		lineOfHtml.setId( "Line of HTML : " );
		
		lineOfHtmlLabel = new Label( "Line of HTML : " );
		lineOfHtmlLabel.setLabelFor( lineOfHtml );
		
		labels.add( actionFieldLabel );
		labels.add( sendKeysFieldLabel );
	     
		textFields.add( keysToSend );
	     
		comboBoxes.add( actionType );
	     
		compsComp = new ArrayList<Node>();
		compsComp.add( actionType );
		compsComp.add( keysToSend );

		VBox vbox = new VBox();
		vbox.setStyle( "height:100%" );
		
		NoirStyleUtilities.iPhoneBackgroundStyle( vbox );
		
	    vbox.setPadding( new Insets( 10 ) );
	    vbox.setSpacing( 8 );

		NoirSwingUtilities.addLabelTextRowsComps( labels, compsComp, vbox );
	     	     
		mSubmit = new Button( "Create Step" );
		NoirStyleUtilities.iPhoneButtonStyle( mSubmit );
		
   	 	vbox.getChildren().add( mSubmit );
   	 	
		listPanel = new ListPanel( FrameType.Avant );
		
		HBox bottomButtons = listPanel.buttonPane();
		ScrollPane listPane = listPanel.listPane();
	    
		listPanel.setListeners();
		
	    mSubmit.setOnMouseClicked( new AvantOnSubmitStepListener( keysToSend, lineOfHtml, listPanel.getListModel(), listPanel.getRunButton(), listPanel ) );

		actionType.getSelectionModel().selectedItemProperty().addListener( new OnComboSwitchListener( actionType, compsComp, 
																labels, keysToSend, 
																actionFieldLabel, sendKeysFieldLabel, 
																lineOfHtmlLabel, vbox, lineOfHtml, this  ) );
		
		setTop( vbox );
		setCenter( listPane );
		setBottom( bottomButtons );
	}
}
