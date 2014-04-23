package com.cafe.noir.util;

import java.io.File;

public class BrowserCheck 
{
	public static boolean isFirefoxEnabled()
	{
		if( new File( "/Applications/Firefox.app/Contents/MacOS/Firefox" ).exists() )
			return true;
		else return false;
	}
	public static boolean isSafariEnabled()
	{
		if( new File( "/Applications/Safari.app/Contents/MacOS/Safari" ).exists() )
			return true;
		else return false;
	}
	public static boolean isChromeEnabled()
	{
		if( new File( "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ).exists() )
			return true;
		else return false;
	}
}
