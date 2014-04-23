package com.cafe.noir.panels.listeners;

import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.scene.control.Button;

public class OnListSelection implements ChangeListener<String>
{
	private Button fireButton;

	public OnListSelection( Button fireButton )
	{
		this.fireButton = fireButton;
	}

	@Override
	public void changed( ObservableValue<? extends String> observable, String oldValue, String newValue) 
	{
		if ( newValue != null ) 
        {
            fireButton.disarm();
        } 
        else 
        {
            fireButton.arm();
        }
	}
}
