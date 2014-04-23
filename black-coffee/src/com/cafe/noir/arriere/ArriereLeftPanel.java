package com.cafe.noir.arriere;

import java.util.ArrayList;

import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import com.cafe.noir.panels.ListPanel;
import com.cafe.noir.panels.listeners.ArriereOnSubmitStepListener;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.NoirStyleUtilities;
import com.cafe.noir.util.NoirSwingUtilities;

public class ArriereLeftPanel extends BorderPane
{
	private TextField urlField;
	private TextField keyField;
	private TextField valueField;
	
	private ArrayList<Label> labels = new ArrayList<Label>();
	
	private Label urlFieldLabel;
	private Label keyValuePairLabel;

	private ArrayList<Node> compsComp;
	public Button mSubmit;
	public static ListPanel listPanel;

    private static final String urlString = "URL: ";
    private static final String kvpString = "KeyValuePairs:";
    
	public ArriereLeftPanel()
	{
		super();
	    
		urlField = new TextField();
		urlField.setId( "URL" );
		
		urlFieldLabel = new Label( urlString );
		urlFieldLabel.setLabelFor( urlField );
		
		keyValuePairLabel = new Label( kvpString );

		keyField = new TextField();
		keyField.setId( "KEY" );
		
		valueField = new TextField();
		valueField.setId( "VALUE" );
		
		HBox horizKVPBox = new HBox();
		horizKVPBox.setSpacing( 8 );
		
		horizKVPBox.getChildren().addAll( keyField, valueField );
		
		labels.add( urlFieldLabel );
		labels.add( keyValuePairLabel );
	     
		compsComp = new ArrayList<Node>();
		compsComp.add( urlField );
		compsComp.add( horizKVPBox );

		VBox vbox = new VBox();
		vbox.setStyle( "height:100%" );
		
		NoirStyleUtilities.iPhoneBackgroundStyle( vbox );
		
	    vbox.setPadding( new Insets( 10 ) );
	    vbox.setSpacing( 8 );

		NoirSwingUtilities.addLabelTextRowsComps( labels, compsComp, vbox );
	    
		Button plusButton = new Button( " + " );
		Button minusButton = new Button( " - " );
				
		HBox hButtonBox = new HBox();
		hButtonBox.setPadding( new Insets( 10 ) );
		hButtonBox.setSpacing( 8 );
		
		hButtonBox.getChildren().addAll( plusButton, minusButton );
		
		mSubmit = new Button( "Create Step" );
		NoirStyleUtilities.iPhoneButtonStyle( mSubmit, plusButton, minusButton );
		
   	 	vbox.getChildren().addAll( hButtonBox, mSubmit );
   	 	
		listPanel = new ListPanel( FrameType.Arriere );
		
		HBox bottomButtons = listPanel.buttonPane();
		ScrollPane listPane = listPanel.listPane();
	    
		listPanel.setListeners();
		
	    mSubmit.setOnMouseClicked( new ArriereOnSubmitStepListener( vbox, listPanel.getListModel(), listPanel.getRunButton(), listPanel ) );
		addPlusMinusListener( plusButton, OnPlusMinusListener.PlusOrMinus.Plus, vbox, horizKVPBox, hButtonBox, urlField, mSubmit );
		addPlusMinusListener( minusButton, OnPlusMinusListener.PlusOrMinus.Minus, vbox, horizKVPBox, hButtonBox, urlField, mSubmit );

		setTop( vbox );
		setCenter( listPane );
		setBottom( bottomButtons );
	}
	
	private void addPlusMinusListener( Button plusOrMinus, OnPlusMinusListener.PlusOrMinus pom, 
									   VBox vbox, HBox horizKVPBox, HBox horizButtonBox, 
									   TextField urlField, Button submit )
	{
		plusOrMinus.setOnMouseClicked( new OnPlusMinusListener( pom,
																labels, 
																compsComp,
																vbox,
																horizKVPBox,
																horizButtonBox, urlField, submit ) );
	}
}
