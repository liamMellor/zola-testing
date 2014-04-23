package com.cafe.noir;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.layout.HBox;

import com.cafe.noir.directeur.DirecteurCenterPanel;
import com.cafe.noir.directeur.DirecteurLeftPanel;
import com.cafe.noir.directeur.DirecteurRightPanel;
import com.cafe.noir.directeur.OnHopperRunListener;
import com.cafe.noir.util.NoirStyleUtilities;

public class DirecteurViewController extends HBox
{
	public DirecteurViewController()
	{
		super();
		
		setAlignment( Pos.CENTER );
		setPadding( new Insets( 20, 20, 20, 20 ) );
	    setSpacing( 100 );
	    
    	NoirStyleUtilities.iPhoneBackgroundStyle( this );

    	DirecteurLeftPanel directeurLeftPanel = new DirecteurLeftPanel();
    	DirecteurCenterPanel directeurCenterPanel = new DirecteurCenterPanel();
    	DirecteurRightPanel directeurRightPanel = new DirecteurRightPanel();

    	directeurCenterPanel.getRunButton().setOnMouseClicked( 
    			new OnHopperRunListener( directeurRightPanel.getTerminal(), 
    									 directeurCenterPanel.getListModel() ) );
    	
		getChildren().add( directeurLeftPanel );
		getChildren().add( directeurCenterPanel );
		getChildren().add( directeurRightPanel );
	}
}
