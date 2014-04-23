package com.cafe.noir.buttons;

import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;

import com.cafe.noir.util.BrowserCheck;

public class BrowserButton extends Button
{
	public enum BrowserType { CHROME, FIREFOX, SAFARI };
	public enum State { INACTIVE, ACTIVE }
	
	private State state;
	
	private static final String CHROME_ICN = "/img/chrome_icn";
	private static final String FIREFOX_ICN = "/img/firefox_icn";
	private static final String SAFARI_ICN = "/img/safari_icn";

	private static final String SELECTED = "_selected";
	private static final String HOVERED = "_hover";
	private static final String SELECTED_HOVERED = "_selected_hover";
	private static final String DISABLED = "_disabled";

	private static final String PNG = ".png";
	
	private ImageView iconInactive;
	private ImageView iconHovered;
	private ImageView iconActive;
	private ImageView iconActiveHovered;

	private double width;
	private double height;
	
	public BrowserButton( BrowserType browserType, double width, double height )
	{
		super();
		
		this.width = width;
		this.height = height;
		
        setStyle( "-fx-background-color:  rgba(0, 0, 0, 0);" );

        setState( State.INACTIVE );
        
        if( isBrowserEnabled( browserType ) )
        {
        	setImages( browserType, false );
    		
    		setGraphic( iconInactive );
    		
			OnMouseEvent onMouseEvent = new OnMouseEvent( this );
			setOnMouseEntered( onMouseEvent );
			setOnMouseExited( onMouseEvent );
			setOnMouseClicked( onMouseEvent );
        }
        else
        {
        	setImages( browserType, true );
    		
        	setOpacity( 0.75 );
        	
    		setGraphic( iconInactive );
    		
        	disarm();
        }
	}
	
	private boolean isBrowserEnabled( BrowserType browserType )
	{
		boolean isEnabled = false;
		switch( browserType )
		{
			case CHROME:
				if( BrowserCheck.isChromeEnabled() )
					isEnabled = true;
				break;
			case FIREFOX:
				if( BrowserCheck.isFirefoxEnabled() )
					isEnabled = true;
				break;
			case SAFARI:
				if( BrowserCheck.isSafariEnabled() )
					isEnabled = true;
				break;
			default:
				break;
		}
		return isEnabled;
	}
	private void setImages( BrowserType browserType, boolean disabled )
	{
		String _ICN = null;
		switch( browserType )
		{
			case CHROME:
				_ICN = CHROME_ICN;
				break;
			case FIREFOX:
				_ICN = FIREFOX_ICN;
				break;
			case SAFARI:
				_ICN = SAFARI_ICN;
				break;
			default:
				break;
		}
		iconInactive = new ImageView( new Image( getClass().getResourceAsStream( disabled ? _ICN + DISABLED + PNG : _ICN + PNG ), width, height, true, true ) );
		iconActive = new ImageView( new Image( getClass().getResourceAsStream( _ICN + SELECTED + PNG ), width, height, true, true ) );
		iconHovered = new ImageView( new Image( getClass().getResourceAsStream( _ICN + HOVERED + PNG ), width, height, true, true ) );
		iconActiveHovered = new ImageView( new Image( getClass().getResourceAsStream( _ICN + SELECTED_HOVERED + PNG ), width, height, true, true ) );
	}
	
	private void setState( State state )
	{
		this.state = state;
	}
	public State getState()
	{
		return this.state;
	}
	
	private class OnMouseEvent implements EventHandler<MouseEvent>
	{
		private Button button;

		public OnMouseEvent( Button button )
		{
			this.button = button;
		}
		
		@Override
		public void handle( MouseEvent e ) 
		{
			if( e.getEventType() == MouseEvent.MOUSE_ENTERED )
			{
				switch( state )
				{
					case ACTIVE:
						button.setGraphic( iconActiveHovered );
						break;
					case INACTIVE:
						button.setGraphic( iconHovered );
						break;
					default:
						break;
				}
			}
			else if( e.getEventType() == MouseEvent.MOUSE_EXITED )
			{
				switch( state )
				{
					case ACTIVE:
						button.setGraphic( iconActive );
						break;
					case INACTIVE:
						button.setGraphic( iconInactive );
						break;
					default:
						break;
				}
			}
			else if( e.getEventType() == MouseEvent.MOUSE_CLICKED )
			{
				switch( state )
				{
					case ACTIVE:
						button.setGraphic( iconInactive );
						setState( State.INACTIVE );
						break;
					case INACTIVE:
						button.setGraphic( iconActive );
						setState( State.ACTIVE );
						break;
					default:
						break;
				}
			}
		}
	}
}
