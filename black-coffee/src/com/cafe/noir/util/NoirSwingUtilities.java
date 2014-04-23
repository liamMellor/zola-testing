package com.cafe.noir.util;

import java.util.ArrayList;

import javafx.scene.Node;
import javafx.scene.control.Label;
import javafx.scene.layout.Pane;

public class NoirSwingUtilities 
{

	public static void addLabelTextRowsComps( ArrayList<Label> labels, ArrayList<Node> compsComp, Pane vbox ) 
	{
		for ( int i = 0; i < labels.size(); i++ )
		{
			labels.get(i).setLabelFor( compsComp.get(i) );
			vbox.getChildren().addAll( labels.get(i), compsComp.get(i) );
		}
	}
	
	public static void genericRemover(ArrayList<Object> a, Object... b )
	{
		for ( Object c: b )
		{
			a.remove( c );
		}
	}
	
	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void genericAdder( ArrayList a, Object... b )
	{
		for ( Object c: b )
		{
			a.add( c );
		}
	}
}
