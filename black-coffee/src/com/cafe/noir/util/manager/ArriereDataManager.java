package com.cafe.noir.util.manager;

import java.io.File;
import java.util.Map;
import java.util.TreeMap;

public class ArriereDataManager 
{
	public static File cgiDir = new File( "jython/cgi" );
	public static TreeMap<Integer, Map<String, Map<String, String>>> constructionMap = new TreeMap<Integer, Map<String, Map<String, String>>>();
}
