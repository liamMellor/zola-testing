package com.cafe.noir.util.manager;

import java.io.File;
import java.util.Map;
import java.util.TreeMap;

import com.cafe.noir.avant.BrowserAction;

public class AvantDataManager 
{
	public static File selDir = new File( "jython/selenium" );
	public static TreeMap<Integer, Map<BrowserAction, String[]>> constructionMap = new TreeMap<Integer, Map<BrowserAction, String[]>>();
}
