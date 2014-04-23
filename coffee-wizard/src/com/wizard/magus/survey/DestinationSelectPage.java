package com.wizard.magus.survey;

import java.io.File;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;
import javafx.scene.text.TextAlignment;
import javafx.stage.DirectoryChooser;
import javafx.stage.Stage;

import com.wizard.magus.WizardPage;
import com.wizard.magus.util.FileManager;

public class DestinationSelectPage extends WizardPage 
{	 
	public DestinationSelectPage() 
	{
		super( "Select a Destination" );
	    
	    labs[2].setGraphic( new ImageView( activeIcn ) );

		nextButton.setDisable( true );
	    finishButton.setDisable( true );
	}

	@Override
	protected Parent getContent() 
	{
		VBox vbox = new VBox();
		vbox.setPadding( new Insets( 20, 20, 20, 20 ) );
		vbox.setSpacing( 20 );
		
		Label fiChooser = new Label( "Choose the location you wish to install Black Coffee" );
		
		fiChooser.setStyle( "-fx-font-size:12px;" );
		
		Label l = new Label( "_________________________________________" );
		
		Button choose = new Button();
		choose.setGraphic( new ImageView( new Image( getClass().getResourceAsStream( "/img/folder_icn.png" ) ) ) );
		choose.setLayoutX( choose.getLayoutX() + 50 );
		File file = new File( "/" );
		long freeSpace = file.getFreeSpace();
		long totalSpace = file.getTotalSpace();
		
		Label chooseLabel = new Label( freeSpace/1073741824 + "GB available\n" +  totalSpace/1073741824 + "GB total" );
		chooseLabel.setTextAlignment( TextAlignment.CENTER );
		chooseLabel.setStyle( "-fx-font-size:12px;" );
		
		chooseLabel.setLabelFor( choose );
		final Label fName = new Label();
		fName.setStyle( "-fx-font-size:12px;" );
		
		Label l2 = new Label( "_________________________________________" );
		
		Label l3 = new Label( "Installing this software requires 20 MB of space." );
		l3.setStyle( "-fx-font-size:12px;" );
		
		choose.setOnAction( new EventHandler<ActionEvent>()
		{
			@Override
			public void handle( ActionEvent arg0 ) 
			{
				DirectoryChooser fileChooser = new DirectoryChooser();
				
				fileChooser.setTitle( "Choose Install Location" );
				File f = fileChooser.showDialog( new Stage() );
				fName.setText( "Black Coffee will install to:\n" + f.getAbsolutePath() );
				FileManager.targetDir = f;
				
				nextButton.setDisable( false );
			}
		});
		
		vbox.getChildren().addAll( fiChooser, l, choose, chooseLabel, l2, l3, fName );
		
	    return vbox;
	}
}
