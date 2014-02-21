package quantum;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map.Entry;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.bouncycastle.util.encoders.Base64;


public class QuantumConstructor {
	
	public static String construct(){
		LinkedHashMap<Integer, LinkedHashMap<String, String>> creatorMap = QuantumDataManager.creatorMap;
		StringBuilder sb = new StringBuilder(64);
		sb.append(
				";;;;;;;;;;;;;;;;;;;;;;\n"+
				";        domain      ;\n"+
				";;;;;;;;;;;;;;;;;;;;;;\n");
		sb.append("\n");
		sb.append(";Full domain\n");
		sb.append("!domain=" + QuantumDataManager.baseClassURL +"\n");
		sb.append("\n");
		sb.append(
				";;;;;;;;;;;;;;;;;;;;;;\n"+
				";      subdomain     ;\n"+
				";;;;;;;;;;;;;;;;;;;;;;\n");
		sb.append("\n");
		sb.append(";End of given url.\n");
		String sub_d = null;
		String[] splitUrl = QuantumDataManager.baseClassURL.split("com");
		if (splitUrl.length == 1){
			sub_d = "index";
		}
		else{
			sub_d = splitUrl[1];
		}
		sb.append("!sub_domain=" + sub_d +"\n");
		sb.append("\n");
		for( Entry<Integer, LinkedHashMap<String, String>> creatorEntries : creatorMap.entrySet()){
			sb.append("$"+creatorEntries.getKey());
			LinkedHashMap<String, String> entryStorage = creatorEntries.getValue();
			int y = 0;
			for( Entry<String, String> innerEntry : entryStorage.entrySet()){
				sb.append("#"+creatorEntries.getKey()+y+innerEntry.getKey()+","+innerEntry.getValue());
			}
			sb.append("\n");
		}
		return sb.toString();
	}

	public static void reconstruct(String everything, boolean reissue) {
		QuantumDataManager.onDestroy();
		byte[] allBytes = Base64.decode(everything.getBytes());
		everything = new String(allBytes);
        Pattern pattern = Pattern.compile("^!domain=+(.*)", Pattern.MULTILINE);

        Matcher matcher = pattern.matcher(everything);
        while (matcher.find()) {
        	String domain = matcher.group();
        	String[] splitDomain = domain.split("=");
        	QuantumDataManager.baseClassURL = splitDomain[1];
        }
        pattern = Pattern.compile("^!sub_domain=+(.*)", Pattern.MULTILINE);
        matcher = pattern.matcher(everything);
        while (matcher.find()) {
        	String subdomain = matcher.group();
        	String[] splitsubDomain = subdomain.split("=");
        	QuantumDataManager.baseClassSubDomain = splitsubDomain[1];
        }
        pattern = Pattern.compile("^\\$+(.*)", Pattern.MULTILINE);
        matcher = pattern.matcher(everything);
        int y = 0;
        LinkedHashMap<String, String> readContainer = new LinkedHashMap<String, String>();
        LinkedHashMap<Integer, LinkedHashMap<String,String>> grandContainer = new LinkedHashMap<Integer, LinkedHashMap<String, String>>();
        while (matcher.find()) {
           // System.out.println(matcher.group());
            String group = matcher.group();
            String[] indyGroup = group.split(",");
            int z = 0;
            ArrayList<String> tempList = new ArrayList<String>();
            for(String line: indyGroup){
            	String newLine = line.replace("#"+y+z, "");
            	newLine = newLine.replace("$"+y, "");
            	if(z == 0){
            		newLine = newLine.replaceAll("\\[^a-zA-Z\\s]", "");
            	}
            	tempList.add(newLine);        	
            	z++;
            }
            String[] tempArray = new String[tempList.size()];
            tempArray = tempList.toArray(tempArray);
            StringBuilder sbCommand = new StringBuilder(64);
            for(String sbVal : tempArray){
            	sbCommand.append(sbVal+",");
            }
            readContainer.put(tempList.get(0), sbCommand.toString().replace(tempList.get(0)+",", ""));
            grandContainer.put(y, readContainer);
            y++;
            readContainer = new LinkedHashMap<String, String>();
        }
        QuantumDataManager.creatorMap = grandContainer;
    	if(reissue){
    		for(int i = 0; i < QuantumDataManager.creatorMap.size(); i++){
    			QuantumCreatorList.listConstructor(i);
    		}
    	}
	}
}
