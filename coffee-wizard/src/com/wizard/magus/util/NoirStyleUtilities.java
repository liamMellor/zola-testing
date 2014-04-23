package com.wizard.magus.util;

import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.Tab;

public class NoirStyleUtilities 
{
	public static void iPhoneButtonStyle( Button... buttons )
	{
		for( Button button : buttons )
			button.getStyleClass().add( "iphone" );
	}
	
	public static void iPhoneButtonStyle( Tab... tabs )
	{
		for( Tab tab : tabs )
			tab.getStyleClass().add( "inner-tab" );
	}
	
	public static void iPhoneBackgroundStyle( Node... nodes )
	{
		for( Node node : nodes )
			node.getStyleClass().add( "iphone-toolbar" );
	}
	public static void warningBackgroundStyle( Node... nodes )
	{
		for( Node node : nodes )
			node.getStyleClass().add( "warning" );
	}
}
