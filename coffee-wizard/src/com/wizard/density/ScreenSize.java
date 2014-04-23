package com.wizard.density;

import javafx.geometry.Rectangle2D;
import javafx.stage.Screen;

public class ScreenSize 
{
	public ScreenSize()
	{
		
	}
	
	public static Rectangle2D getScreenSize()
	{
		return Screen.getPrimary().getVisualBounds();
	}
}
