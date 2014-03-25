package quantum;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.TreeMap;

import javax.swing.JFrame;

public class APIshDataManager {
	public static JFrame frame = new JFrame("QuANTUM Creator");
	
	public static String currentUrl = "http://bookish.com";
	
	public static ArrayList<String> requestType = new ArrayList<String>();
	public static ArrayList<String> urlUp = new ArrayList<String>();
	public static TreeMap<Integer, LinkedHashMap<String, String>> creationContainer = new TreeMap<Integer, LinkedHashMap<String, String>>();
	public static LinkedHashMap<String, String> managerContainer = new LinkedHashMap<String , String>();
	
	public static TreeMap<Integer, LinkedHashMap<String, String>> creatorMap = new TreeMap<Integer, LinkedHashMap<String, String>>();
	
	public static String className = new String();
	
	public static String baseClassURL = new String();
	public static String baseClassSubDomain = new String();
	public static String runnerConsole = "";
	
	public static void onDestroy(){
		//currentUrl = "http://bookish.com";
		creationContainer.clear();
		className = "";
		baseClassURL = "";
		baseClassSubDomain = "";
		runnerConsole = "";
		requestType.clear();
		urlUp.clear();
	}
	
}