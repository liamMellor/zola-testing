package com.cafe.noir.avant.jython;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import com.cafe.noir.arriere.ArriereLeftPanel;
import com.cafe.noir.avant.AvantLeftPanel;
import com.cafe.noir.avant.BrowserAction;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.manager.ArriereDataManager;
import com.cafe.noir.util.manager.AvantDataManager;
import com.cafe.noir.util.manager.FileManager;

public class JythonReader 
{
	FrameType ft;
	
	public JythonReader( File file )
	{
		String fileString = null;
		try 
		{
			FileInputStream fis = new FileInputStream( file );
			fileString = FileManager.inputStreamToString( fis, false );
		} 
		catch ( FileNotFoundException e ) 
		{
			e.printStackTrace();
		} 
		catch (IOException e) 
		{
			e.printStackTrace();
		}
		
		if( fileString.contains( "from selenium import webdriver" ) )
		{
			AvantDataManager.constructionMap.clear();
			AvantLeftPanel.listPanel.getListModel().clear();
			
			ft = FrameType.Avant;
			Pattern pattern = Pattern.compile ( "(?m)^.*$", Pattern.MULTILINE );

			int index = 0;

	        Matcher matcher = pattern.matcher( fileString );
	        int matches = 0;
	        while ( matcher.find() ) 
	        {
	        	String line = matcher.group();
	        	if( line.contains( ".get" ) )
	        	{
	    			index++;
	    			Map<BrowserAction, String[]> map = new HashMap<BrowserAction, String[]>();
	    			map.put( BrowserAction.GoTo, new String[]{ line.split( "\"" )[1] } );
	    			AvantDataManager.constructionMap.put( index, map );
	    			avantListConstructor( line.split( "\"" )[1], BrowserAction.GoTo, index );
	        	}
	        	else if( line.contains( ".send_keys") && line.contains( ".submit()" ) )
	        	{
	    			index++;
	        		Map<BrowserAction, String[]> map = new HashMap<BrowserAction, String[]>();
	    			map.put( BrowserAction.EnterTextAndSubmit, new String[]{ line.split( "\"" )[1], matcher.group( matches + 1 ).split( "\"" )[1] } );
	    			AvantDataManager.constructionMap.put( index, map );
	    			avantListConstructor( line.split( "\"" )[1] + "\nKeys to send and Submit: " 
							+ matcher.group( matches + 1 ).split( "\"" )[1], 
							BrowserAction.EnterTextAndSubmit, 
							index );
	        	}
	        	else if( line.contains( ".send_keys") )
	        	{
	    			index++;
	        		Map<BrowserAction, String[]> map = new HashMap<BrowserAction, String[]>();
	    			map.put( BrowserAction.EnterText, new String[]{ line.split( "\"" )[1] } );
	    			AvantDataManager.constructionMap.put( index, map );
	    			avantListConstructor( line.split( "\"" )[1], BrowserAction.EnterText, index );
	        	}
	        	else if( line.contains( ".click()") )
	        	{
	    			index++;
	        		Map<BrowserAction, String[]> map = new HashMap<BrowserAction, String[]>();
	    			map.put( BrowserAction.Click, new String[]{ line.split( "\"" )[1] } );
	    			AvantDataManager.constructionMap.put( index, map );
	    			avantListConstructor( line.split( "\"" )[1], BrowserAction.Click, index );
	        	}
	        	matches++;
	        }
	        AvantLeftPanel.listPanel.setCurrentListNumber( index );
		}
		else if( fileString.contains( "import urllib" ) )
		{
			ArriereDataManager.constructionMap.clear();
			ArriereLeftPanel.listPanel.getListModel().clear();

			ft = FrameType.Arriere;
			Pattern pattern = Pattern.compile ( "(?m)^.*$", Pattern.MULTILINE );

			int index = 0;

	        Matcher matcher = pattern.matcher( fileString );
	        
	        Map<String, Map<String, String>> urlAndKvpMap = null;
			Map<String, String> kvpMap = null;
			String url = null;
			
	        while ( matcher.find() ) 
	        {
	        	String line = matcher.group();
	        	if( line.contains( "url =" ) )
	        	{
	        		index++;
	    			urlAndKvpMap = new HashMap<String, Map<String,String>>();
	    			kvpMap = new HashMap<String, String>();
	    			
	    			url = line.split( "\"" )[1];
	    			continue;
	        	}
	        	else if( line.contains( "vals =" ) )
	        	{
	        		String vals = matcher.group().split( "= " )[1];
	        		vals = vals.replace( "{", "" ).replace( "}", "" );
	    			String[] kvps = vals.split( "," );
	    			for( String pair : kvps )
	    			{
	    				String[] kvp = pair.split( " : " );
	    				kvpMap.put( kvp[0].replace( "'", ""), kvp[1].replace( "'", "" ) );
	    			}
	    			arriereListConstructor( url, kvpMap, index );
	    			urlAndKvpMap.put( url, kvpMap );
	    			
	    			ArriereDataManager.constructionMap.put( index, urlAndKvpMap );
	        	}
	        }
	        ArriereLeftPanel.listPanel.setCurrentListNumber( index );
		}
	}

	
	private void avantListConstructor( String lineToSend, BrowserAction curAction, int index )
	{
		StringBuilder sb = new StringBuilder( 64 );
		sb.append( "Step " + index + "\n" );
		sb.append( "Action: " + curAction + "\n" );
		sb.append( "Line to send: " + lineToSend);
		AvantLeftPanel.listPanel.getListModel().add( sb.toString() );
	}
	
	private void arriereListConstructor( String url, Map<String, String> kvps, int index )
	{
		StringBuilder sb = new StringBuilder();
		sb.append( "Step " + index + "\n" );
		sb.append( "URL: " + url + "\n" );
		sb.append( "KeyValuePairs:\n" );
		for( Entry<String, String> kvp : kvps.entrySet() )
		{
			sb.append( "     " + kvp.getKey() + " , " + kvp.getValue() + "\n" );
		}
		ArriereLeftPanel.listPanel.getListModel().add( sb.toString() );
	}
	public FrameType getFrameType()
	{
		return ft;
	}
}
