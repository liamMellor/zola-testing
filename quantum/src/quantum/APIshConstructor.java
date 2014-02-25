package quantum;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map.Entry;
import java.util.Set;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.bouncycastle.util.encoders.Base64;


public class APIshConstructor {
	public static String construct(){
		
		TreeMap<Integer, LinkedHashMap<String, String>> creationContainer = APIshDataManager.creationContainer;
		StringBuilder sb = new StringBuilder(64);
		sb.append(
				";;;;;;;;;;;;;;;;;;;;;;\n"+
				";        domain      ;\n"+
				";;;;;;;;;;;;;;;;;;;;;;\n");
		sb.append("\n");
		sb.append(";Full domain\n");
		sb.append("!domain=" + APIshDataManager.baseClassURL +"\n");
		sb.append("\n");
		sb.append(
				";;;;;;;;;;;;;;;;;;;;;;\n"+
				";      subdomain     ;\n"+
				";;;;;;;;;;;;;;;;;;;;;;\n");
		sb.append("\n");
		sb.append(";End of given url.\n");
		String sub_d = null;
		String[] splitUrl = APIshDataManager.baseClassURL.split("com");
		if (splitUrl.length == 1){
			sub_d = "index";
		}
		else{
			sub_d = splitUrl[1];
		}
		sb.append("!sub_domain=" + sub_d +"\n");
		sb.append("\n");
		int z = 0;
		
		Set<Entry<Integer, LinkedHashMap<String, String>>> entrySet = creationContainer.entrySet();
		for(Entry<Integer, LinkedHashMap<String, String>> keyValuePair: entrySet){
			sb.append("$"+z);
			sb.append("#"+z+keyValuePair.getValue().keySet().toString());
			sb.append("#"+z+keyValuePair.getValue().entrySet().toString());
			z++;
		}
		
		return sb.toString();	
	}
	
	public static void reconstruct(String everything, boolean reissue) {
		APIshDataManager.onDestroy();
		byte[] allBytes = Base64.decode(everything.getBytes());
		everything = new String(allBytes);
        Pattern pattern = Pattern.compile("^!domain=+(.*)", Pattern.MULTILINE);

        Matcher matcher = pattern.matcher(everything);
        while (matcher.find()) {
        	String domain = matcher.group();
        	String[] splitDomain = domain.split("=");
        	APIshDataManager.baseClassURL = splitDomain[1];
        }
        pattern = Pattern.compile("^!sub_domain=+(.*)", Pattern.MULTILINE);
        matcher = pattern.matcher(everything);
        while (matcher.find()) {
        	String subdomain = matcher.group();
        	String[] splitsubDomain = subdomain.split("=");
        	APIshDataManager.baseClassSubDomain = splitsubDomain[1];
        }
        pattern = Pattern.compile("^\\$+(.*)", Pattern.MULTILINE);
        matcher = pattern.matcher(everything);
        int y = 0;
        ArrayList<String> readContainer = new ArrayList<String>();                         
        TreeMap<Integer, HashMap<String, String>> readMap = new TreeMap<Integer, HashMap<String,String>>();
        while (matcher.find()) {
           // System.out.println(matcher.group());
            String group = matcher.group();
            String[] indyGroup = group.split(",");
            int z = 0;
            ArrayList<String> tempList = new ArrayList<String>();
            for(String line: indyGroup){
            	String newLine = line.replace("#"+y+z, "");
            	readContainer.add(newLine);
            	if(z % 2 != 0){
            		HashMap<String, String> n = new HashMap<String, String>();
            		n.put(readContainer.get(0), readContainer.get(1));
            		readMap.put( readMap.size(), n);
            		readContainer.clear();
            	}
            	tempList.add(newLine);
            	z++;
            }
        }
        APIshDataManager.creatorMap = readMap;
    	if(reissue){
    		for(int i = 0; i < APIshDataManager.creatorMap.size(); i++){
    			APIshCreatorList.listConstructor(i);
    		}
    	}
        
	}
}
