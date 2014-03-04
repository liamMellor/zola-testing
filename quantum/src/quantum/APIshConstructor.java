package src.quantum;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map.Entry;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.bouncycastle.util.encoders.Base64;


public class APIshConstructor {
	private static Object test;

	public static String construct(){
		
		TreeMap<Integer, LinkedHashMap<String, String>> creationContainer = APIshDataManager.creationContainer;
		ArrayList<String> requestType = APIshDataManager.requestType;
		ArrayList<String> urlUp = APIshDataManager.urlUp;
		StringBuilder sb = new StringBuilder(64);
		
		int i = 0;
		
		while(i < creationContainer.size()){
			sb.append(i + "\n");
			sb.append("!RequestType=");
			sb.append(requestType.get(i) + "\n");
			
			sb.append("!URL=");
			sb.append(urlUp.get(i)+ "\n");
			
			LinkedHashMap<String, String> x = creationContainer.get(i);
	
			sb.append("$");
			for(Entry<String, String> keyValuePair: x.entrySet()){
				sb.append("#" + keyValuePair.getKey() + ",");
				sb.append("#" + keyValuePair.getValue() + ",");
			}			
			i++;
			
		}
		
		return sb.toString();	
	}
	
	public static void reconstruct(String everything, boolean reissue) {
		APIshDataManager.onDestroy();
		//byte[] allBytes = Base64.decode(everything.getBytes());
		//everything = new String(allBytes);
        Pattern pattern = Pattern.compile("^!RequestType=+(.*)", Pattern.MULTILINE);

        Matcher matcher = pattern.matcher(everything);
        while (matcher.find()) {
        	String domain = matcher.group();
        	String[] splitRequest = domain.split("=");
        	APIshDataManager.requestType.add(splitRequest[1]);
        }
        pattern = Pattern.compile("^!URL=+(.*)", Pattern.MULTILINE);
        matcher = pattern.matcher(everything);
        while (matcher.find()) {
        	String subdomain = matcher.group();
        	String[] splitURL = subdomain.split("=");
        	APIshDataManager.urlUp.add(splitURL[1]);
        }
        pattern = Pattern.compile("^\\$+(.*)", Pattern.MULTILINE);
        matcher = pattern.matcher(everything);
        ArrayList<String> readContainer = new ArrayList<String>();                         
        TreeMap<Integer, LinkedHashMap<String, String>> readMap = new TreeMap<Integer, LinkedHashMap<String,String>>();
        while (matcher.find()) {
           // System.out.println(matcher.group());
            String group = matcher.group();
            String[] indyGroup = group.split(",");
            int z = 0;
            LinkedHashMap<String, String> n = new LinkedHashMap<String, String>();
            for(String line: indyGroup){
            	line = line.replaceAll("#", "");
            	line = line.replaceAll("\\$", "");
            	readContainer.add(line);
            	if(z % 2 != 0){
            		n.put(readContainer.get(0), readContainer.get(1));
            		readContainer.clear();
            	}
            	z++;
            }
            readMap.put(readMap.size(), (LinkedHashMap<String, String>) n.clone());
            n.clear();

            
        }
        APIshDataManager.creationContainer = readMap;
    	if(reissue){
    		for(int i = 0; i < APIshDataManager.creationContainer.size(); i++){
    			APIshCreatorList.listConstructor(i);
    		}
    	}
        
	}
}
