package com.wizard.magus.dialogs;

import javafx.scene.Scene;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

public class BaseDialog extends Stage 
{
    public BaseDialog( String title, Stage owner, Scene scene ) 
    {
        setTitle( title );
        initStyle( StageStyle.UTILITY );
        initModality( Modality.APPLICATION_MODAL );
        initOwner( owner );
        setResizable( false );
		scene.getStylesheets().add( this.getClass().getResource( "/css/styles.css" ).toExternalForm() );
        setScene( scene );
    }
    public void showDialog() 
    {
        sizeToScene();
        centerOnScreen();
        showAndWait();
    }
}
