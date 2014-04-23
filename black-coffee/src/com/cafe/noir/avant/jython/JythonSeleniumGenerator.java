package com.cafe.noir.avant.jython;

import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Attribute;
import org.jsoup.nodes.Attributes;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import com.cafe.noir.avant.BrowserAction;
import com.cafe.noir.util.manager.AvantDataManager;

public class JythonSeleniumGenerator 
{
	public static final String INDENT = "     ";
	public static final String[] IMPORTS = { "from selenium import webdriver",
											 "from selenium.webdriver.common.by import By",
											 "from selenium.webdriver.common.action_chains import ActionChains",
											 "from selenium.webdriver.support import expected_conditions as EC" };
	
	private int varInst;
	
	private int stateCheck;
	private ArrayList<String> browserList;
	
	public JythonSeleniumGenerator( boolean chromeCheck, boolean firefoxCheck, boolean safariCheck, int stateCheck )
	{
		this.stateCheck = stateCheck;
		
		browserList = new ArrayList<String>();
		if( chromeCheck )
			browserList.add( "driver = webdriver.Chrome('libs/chromedriver')" );
		if( firefoxCheck )
			browserList.add( "driver = webdriver.Firefox()" );
		if( safariCheck )
			browserList.add( "driver = webdriver.Safari('libs/selenium-server-standalone-2.41.0.jar')" );
	}
	
	public String initJython()
	{
		StringBuilder sb = new StringBuilder();
		
		for( String imports: IMPORTS )
		{
			sb.append( imports + "\n");
		}
		sb.append( "for browser in range(0," + stateCheck + "):\n" );
		sb.append( INDENT + "driver = None\n" );
		for( int i = 0; i < stateCheck; i++ )
		{
			sb.append( INDENT + "if browser is "+i+":\n" );
			sb.append( INDENT + INDENT + browserList.get( i ) + "\n" );
		}
		sb.append( INDENT + "try:\n" );
		for ( Entry<Integer, Map<BrowserAction, String[]>> entrySet : AvantDataManager.constructionMap.entrySet() )
		{
			for( Entry<BrowserAction, String[]> innerEntry : entrySet.getValue().entrySet() )
			{
				switch( innerEntry.getKey() )
				{
					case Click:
						sb.append( INDENT + INDENT + htmlToSelectorGen( innerEntry.getValue()[0] ) + ".click()\n" );
						break;
					case EnterText:
						sb.append( INDENT + INDENT + htmlToSelectorGen( innerEntry.getValue()[0] ) 
								+ ".send_keys(\"" + innerEntry.getValue()[1] + "\")\n" );
						break;
					case EnterTextAndSubmit:
						sb.append( INDENT + INDENT + "ele" + varInst + "=" + htmlToSelectorGen( innerEntry.getValue()[0] ) 
								+ "\n"+ INDENT + INDENT + "ele" +varInst+".send_keys(\"" + innerEntry.getValue()[1] + "\")"
										+ "\n"+ INDENT + INDENT + "ele" +varInst+".submit()\n" );
						varInst++;
						break;
					case GoTo:
						sb.append( INDENT + INDENT + "driver.get(\""+innerEntry.getValue()[0]+"\")\n" );
						break;
					default:
						break;
				}
			}
			sb.append( INDENT + INDENT + "print \"Step " + entrySet.getKey() + " Complete\"\n" );
		}
		sb.append( INDENT + "except Exception as e:\n" );
		sb.append( INDENT + INDENT + "print e\n" );
		sb.append( INDENT + "finally:\n" );
		sb.append( INDENT + INDENT + "driver.quit()" );
		return sb.toString();
	}
	private String htmlToSelectorGen( String html )
	{
		StringBuilder sb = new StringBuilder();
		
		char[] chars = html.toCharArray();
		StringBuilder tagBuilder = new StringBuilder();
		for( char c : chars )
		{
			if ( c != "<".toCharArray()[0] && c != " ".toCharArray()[0] )
				tagBuilder.append( c );
			else if ( c == " ".toCharArray()[0] )
				break;
		}
		
		String tag = tagBuilder.toString();
		
		Document lineOfHtml = Jsoup.parseBodyFragment( html, "ASCII" );
        Element body = lineOfHtml.body();
        Elements eles = body.getElementsByTag( tag );
        
        if( eles.size() == 0 )
        {
        	sb.append( "driver.find_element_by_xpath(\""+html+"\")" );
        }
        else
        {
	        Attributes attributes = eles.get(0).attributes();

			sb.append( "driver.find_element_by_xpath(\"" + buildXpath( attributes, tag ) + "\")");
			/*for( Attribute attr : attributes )
			{
				if( attr.getKey().equals( "id" ) )
				{
					sb.append( "driver.find_element_by_id(\""+attr.getValue()+"\")" );
					break;
				}
				else if( !attr.getKey().trim().equals( "type".trim() )
						&& !attr.getKey().trim().equals( "name".trim() )
						&& !attr.getKey().trim().equals( "style".trim() )
						&& !attr.getKey().trim().equals( "height".trim() )
						&& !attr.getKey().trim().equals( "width".trim() ) )
				{
					sb.append( "driver.find_element_by_css_selector(\""+tag+"["+attr.getKey()+"='"+attr.getValue()+"']\")" );
					break;
				}
			}*/
        }
		return sb.toString();
	}
	
	private String buildXpath( Attributes attributes, String tag )
	{
		StringBuilder sb = new StringBuilder();
		boolean tagAdded = false;
		for( Attribute attr : attributes )
		{
			if( attr.getKey().equals( "id" ) )
				sb.append( "#" + attr.getValue() + " " );
			else if ( attr.getKey().equals( "class" ) )
			{
				if( attr.getValue().contains( " " ) )
				{
					String[] val = attr.getValue().split( " " );
					for( String v : val )
						sb.append( "." + v );
					sb.append( " " );
				}
			}
			else
			{
				sb.append( !tagAdded ? "//" + tag : "" );
				tagAdded = true;
				sb.append( "[@" +attr.getKey()+"='"+attr.getValue()+"']" );
			}
		}
		return sb.toString();
	}
}
