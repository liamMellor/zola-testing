package com.cafe.noir.util.webkit;

import javafx.event.EventHandler;
import javafx.scene.input.ZoomEvent;

public class OnZoomListener implements EventHandler<ZoomEvent>
{
	private Engine engine;
	
	public OnZoomListener( Engine eng ) 
	{
		this.engine = eng;
	}

	@Override
	public void handle( ZoomEvent zoomEvent ) 
	{
		engine.setZoom( zoomEvent.getZoomFactor() );
		zoomEvent.consume();
	}

}
