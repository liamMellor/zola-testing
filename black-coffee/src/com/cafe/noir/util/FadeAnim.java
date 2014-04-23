package com.cafe.noir.util;

import javafx.concurrent.Task;

import com.cafe.noir.util.Toaster.Dialog;

public class FadeAnim extends Task<Void>
{
	private volatile float opacity = 0f;

    private Dialog dial;

	public FadeAnim( final Dialog dial )
	{
		this.dial = dial;
	}
	
	@Override
	protected Void call() throws Exception 
	{
		fadeIn();
		return null;
	}
	
	private void fadeIn()
	{
		while( opacity != 1f )
		{
			opacity += 0.05f;
            dial.setOpacity( opacity <= 1f ? opacity : 1f );
			try 
        	{
				Thread.sleep( 25 );
			} 
        	catch ( InterruptedException e1 ) 
        	{
				e1.printStackTrace();
			}
			if( opacity >= 1f ) break;
		}
    	try 
    	{
			Thread.sleep( 1000 );
		} 
    	catch ( InterruptedException e1 ) 
    	{
			e1.printStackTrace();
		}
    	finally
    	{
    		fadeOut( dial );
    	}
	}
	
	private void fadeOut( final Dialog dial ) 
    {
		while( opacity != 0f )
		{
			opacity -= 0.05f;
            dial.setOpacity( opacity <= 0 ? 0 : opacity );
            try 
        	{
				Thread.sleep( 25 );
			} 
        	catch ( InterruptedException e1 ) 
        	{
				e1.printStackTrace();
			}
			if( opacity <= 0f ) break;
		}
    	try 
    	{
			Thread.sleep( 1000 );
		} 
    	catch ( InterruptedException e1 ) 
    	{
			e1.printStackTrace();
		}
    	finally
    	{
    		dial.close();
    	}
    }
}