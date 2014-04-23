package com.cafe.noir.arriere.interfaces;

import java.util.ArrayList;
import java.util.List;

import javafx.collections.ObservableList;
import javafx.scene.Node;
import javafx.scene.layout.HBox;

public interface NodeSwitcher 
{
	/**
	 * 
	 * @param children
	 *  : All child nodes of the existing text fields.
	 * @return List of all old key value pairs.
	 */
	List<ArrayList<String>> storeOldValues( ObservableList<Node> children );
	
	/**
	 * 
	 * @param keyString
	 * 	: Old key string to apply to new text fields.
	 * @param valString
	 * 	: Old value string to apply to new text fields.
	 * @return New HBox for addition to parent node.
	 */
	HBox hboxClone( String keyString, String valString );
}
