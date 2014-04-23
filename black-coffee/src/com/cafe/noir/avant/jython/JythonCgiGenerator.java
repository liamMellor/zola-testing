package com.cafe.noir.avant.jython;

import java.util.Map;
import java.util.Map.Entry;

import com.cafe.noir.util.manager.ArriereDataManager;

public class JythonCgiGenerator 
{
	public static final String INDENT = "     ";
	public static final String[] IMPORTS = { "import urllib",
											 "import urllib2",
											 "import json" };
		
	public JythonCgiGenerator()
	{
	}
	
	public String initJython()
	{
		StringBuilder sb = new StringBuilder();
		
		for( String imports: IMPORTS )
		{
			sb.append( imports + "\n");
		}
		
		for ( Entry<Integer, Map<String, Map<String, String>>> entrySet : ArriereDataManager.constructionMap.entrySet() )
		{
			sb.append( "def func" + entrySet.getKey() +"():\n" );
			sb.append( INDENT + "url = \"" + entrySet.getValue().entrySet().iterator().next().getKey() + "\"\n" );
			sb.append( INDENT + "vals = {" );

			for( Entry<String, String> ies : entrySet.getValue().entrySet().iterator().next().getValue().entrySet() )
			{
				sb.append( "'" + ies.getKey() + "' : '" + ies.getValue() + "'," );
			}
			sb.replace( sb.length() -1, sb.length(), "" );
			sb.append( "}\n" );
			sb.append( INDENT + "data = urllib.urlencode(vals)\n" );
			sb.append( INDENT + "req = urllib2.Request(url,data)\n" );
			sb.append( INDENT + "try:\n" );
			sb.append( INDENT + INDENT + "resp = urllib2.urlopen(req)\n" );
			sb.append( INDENT + INDENT + "try:\n" );
			sb.append( INDENT + INDENT + INDENT + "mjson = json.load(resp)\n" );
			sb.append( INDENT + INDENT + INDENT + "print json.dumps(mjson, indent=4, sort_keys=False)\n" );
			sb.append( INDENT + INDENT + INDENT + "return mjson\n" );
			sb.append( INDENT + INDENT + "except ValueError as e:\n" );
			sb.append( INDENT + INDENT + INDENT + "return resp.read()\n" );
			sb.append( INDENT + "except urllib2.URLError as e:\n" );
			sb.append( INDENT + INDENT + "print e\n" );
			sb.append( INDENT + INDENT + "print e.code\n" );
			sb.append( INDENT + INDENT + "print e.read()\n" );
			sb.append( "func" + entrySet.getKey() + "()\n" );
		}
		return sb.toString();
	}
}
