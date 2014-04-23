package com.cafe.noir.panels;


import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.SelectionMode;
import javafx.scene.control.SplitPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;

import com.cafe.noir.panels.listeners.OnFireListener;
import com.cafe.noir.panels.listeners.OnListSelection;
import com.cafe.noir.panels.listeners.OnRunListener;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.NoirStyleUtilities;

public class ListPanel
{
	final static String moveUpString = "Edit";
    final static String runAllString = "Run All";
    final static String fireString = "Remove";

    private int currentListNumber;
	private FrameType ft;
	
    public ListPanel( FrameType ft ) 
    {
    	super();
    	this.ft = ft;
    }
    
    public SplitPane initSplitPane()
    {
    	 SplitPane splitPane = new SplitPane();
    	 final StackPane sp1 = new StackPane();

    	 sp1.getChildren().add( listPane() );
    	 final StackPane sp2 = new StackPane();
    	 sp2.getChildren().add( buttonPane() );
    	 
    	 setListeners();
    	 
    	 splitPane.getItems().addAll( sp1, sp2 );
    	 return splitPane;
    }
    
    private Button fireButton;
    private Button moveUpButton;
    private Button runAllButton;

    private ObservableList<String> listModel;
    private ListView<String> listView;
    
    public HBox buttonPane()
    {      
    	fireButton = new Button( fireString );
    	moveUpButton = new Button( moveUpString );
        runAllButton = new Button( runAllString );
        
        fireButton.setId( fireString );
        
        moveUpButton.setId( moveUpString );
        
        runAllButton.setId( runAllString );
        
        NoirStyleUtilities.iPhoneButtonStyle( fireButton, moveUpButton, runAllButton );
        
    	HBox buttonPane = new HBox();
        buttonPane.setPadding( new Insets( 15, 12, 15, 12 ) );
    	buttonPane.setSpacing( 40 );
        buttonPane.setAlignment( Pos.CENTER );
        
    	NoirStyleUtilities.iPhoneBackgroundStyle( buttonPane );
        
        buttonPane.getChildren().add( fireButton );
        buttonPane.getChildren().add( moveUpButton );
        buttonPane.getChildren().add( runAllButton );
        
        fireButton.disarm();
        moveUpButton.disarm();
        runAllButton.disarm();
        
        runAllButton.setOnMouseClicked( new OnRunListener( ft ) );
                
        return buttonPane;
    }
    
    public ScrollPane listPane()
    {
    	listModel = FXCollections.observableArrayList();

        listView = new ListView<String>( listModel );
        listView.getSelectionModel().setSelectionMode( SelectionMode.MULTIPLE );

        ScrollPane listScrollPane = new ScrollPane();

        listScrollPane.setContent( listView );
        listScrollPane.setFitToWidth( true );
        listScrollPane.setFitToHeight( true );
        
        return listScrollPane;
    }
    
    public void setListeners()
    {
        listView.getSelectionModel().selectedItemProperty().addListener( new OnListSelection( fireButton ) );
        fireButton.setOnMouseClicked( new OnFireListener( listView, listModel, runAllButton, this, ft ) );
    }

	public int getCurrentListNumber() 
	{
		return currentListNumber;
	}

	public void setCurrentListNumber( int currentListNumber ) 
	{
		this.currentListNumber = currentListNumber;
	}
	
	public ObservableList<String> getListModel()
	{
		return listModel;
	}
	
	public ListView<String> getJList()
	{
		return listView;
	}
	
	public Button getRunButton()
	{
		return runAllButton;
	}
}