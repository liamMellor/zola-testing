package com.wizard.magus.dialogs;

import javafx.scene.paint.Color;
import javafx.scene.text.Text;

public class Message extends Text 
{
    public Message( String msg ) 
    {
        super( msg );
        setWrappingWidth( 250 );
        setFill( Color.WHITE );
    }
}
