package com.cafe.noir.arriere;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import com.cafe.noir.arriere.interfaces.NodeSwitcher;
import com.cafe.noir.util.NoirSwingUtilities;

public class OnPlusMinusListener implements EventHandler<MouseEvent>, NodeSwitcher
{
	/**
	 * 
	 * @author Jay
	 *	@enum
	 *	Enumerates whether instance is plus or minus.
	 *	Must supply with constructor.
	 */
	public enum PlusOrMinus
	{
		Plus,
		Minus
	}

	private PlusOrMinus pom;
	private ArrayList<Label> labels;
	private ArrayList<Node> compsComp;
	
	private VBox vbox;
	private HBox hboxKVP;
	
	private TextField urlField;
	private HBox hboxButtons;
	private Button submit;
	
	public OnPlusMinusListener( PlusOrMinus pom2, ArrayList<Label> labels2,
								ArrayList<Node> compsComp2, VBox vbox,
								HBox horizKVPBox, HBox hboxButtons,
								TextField urlField2, Button submit ) 
	{
		this.pom = pom2;
		this.labels = labels2;
		this.compsComp = compsComp2;
		this.vbox = vbox;
		this.hboxKVP = horizKVPBox;
		this.hboxButtons = hboxButtons;
		this.urlField = urlField2;
		this.submit = submit;
	}

	@Override
	public void handle( MouseEvent arg0 ) 
	{
		int compsCount = compsComp.size();

		List<ArrayList<String>> oldValuesList = storeOldValues( vbox.getChildren() );
		ArrayList<String> oldKeys = oldValuesList.get( 0 );
		ArrayList<String> oldVals = oldValuesList.get( 1 );

		compsComp.clear();
		vbox.getChildren().removeAll( vbox.getChildren() );
		vbox.getChildren().clear();
		
		switch( pom )
		{
			case Minus:
				for( int i = 0; i <= compsCount - 2; i++ )
				{
					if( compsCount - 2 != 0 )
						if( i == 0 ) compsComp.add( urlField );
						else if ( i > 0 && i < 2 )
						{
							compsComp.add( hboxKVP );
							NoirSwingUtilities.addLabelTextRowsComps( labels, compsComp, vbox );
						}
						else 
						{
							compsComp.add( hboxKVP );
							HBox clone = hboxClone( 
									oldKeys.get( i - 1 ), 
									oldVals.get( i - 1 ) );
							vbox.getChildren().add( clone );
						}
					else
					{
						compsComp.add( urlField );
						compsComp.add( hboxKVP );
						
						NoirSwingUtilities.addLabelTextRowsComps( labels, compsComp, vbox );
					}
				}
				vbox.getChildren().addAll( hboxButtons, submit );
				break;
			case Plus:
				for( int i = 0; i <= compsCount; i++ )
				{
					if( i == 0 ) compsComp.add( urlField );
					else if ( i > 0 && i < 2 )
					{
							compsComp.add( hboxKVP );
							NoirSwingUtilities.addLabelTextRowsComps( labels, compsComp, vbox );
					}
					else 
					{
						compsComp.add( hboxKVP );
						HBox clone = hboxClone( 
								i == compsCount ? "" : oldKeys.get( i - 1 ), 
								i == compsCount ? "" : oldVals.get( i - 1 ) );
						vbox.getChildren().add( clone );
					}
				}
				vbox.getChildren().addAll( hboxButtons, submit );
				break;
			default:
				break;
		}
	}
	
	@Override
	public List<ArrayList<String>> storeOldValues( ObservableList<Node> children )
	{
		ArrayList<String> oldKeys = new ArrayList<String>();
		ArrayList<String> oldVals = new ArrayList<String>();
		for( Node childNode : children )
		{
			if ( childNode instanceof HBox )
			{
				for( Node hboxChild : ((HBox)childNode).getChildren() )
				{
					
					if( hboxChild instanceof TextField && hboxChild.getId().equals( "KEY" ) )
						oldKeys.add( ((TextField)hboxChild).getText() );
					else if ( hboxChild instanceof TextField && hboxChild.getId().equals( "VALUE" ) )
						oldVals.add( ((TextField)hboxChild).getText() );
				}
			}
		}
		return Arrays.asList( oldKeys, oldVals );
	}
	
	@Override
	public HBox hboxClone( String keyString, String valString )
	{
		HBox newHbox = new HBox();
		newHbox.setSpacing( 8 );
		
		TextField keyField = new TextField();
		keyField.setId( "KEY" );
		keyField.setText( keyString );
		
		TextField valueField = new TextField();
		valueField.setId( "VALUE" );
		valueField.setText( valString );
		
		newHbox.getChildren().addAll( keyField, valueField );
		
		return newHbox;
	}
}
