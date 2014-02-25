package quantum;

import java.util.ArrayList;
import java.util.LinkedHashMap;

import javax.swing.JFrame;

public class QuantumDataManager {
	public static JFrame frame = new JFrame("QuANTUM Creator");
	
	public static String currentUrl = "http://bookish.com";
	
	public static ArrayList<String[]> creationContainer = new ArrayList<String[]>();
	public static LinkedHashMap<String, String> managerContainer = new LinkedHashMap<String , String>();
	
	public static LinkedHashMap<Integer, LinkedHashMap<String, String>> creatorMap = new LinkedHashMap<Integer, LinkedHashMap<String, String>>();
	
	public static boolean managerActive = false;
	
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
	}
	
}
