package quantum;

import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class QuantumConstructor {
	public static String contruct(){
		
		ArrayList<String[]> creationContainer = QuantumDataManager.creationContainer;
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
		int z = 0;
		for(String[] creator : creationContainer){
			sb.append("$"+z);
			int y = 0;
			for(String pack : creator){
				sb.append("#"+z+y+pack+",");
				y++;
			}
			sb.append("\n");
			z++;
		}

		return sb.toString();	
	}
	public static void reconstruct(String everything, boolean reissue) {
		QuantumDataManager.onDestroy();
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
        ArrayList<String> readContainer = new ArrayList<String>();
        while (matcher.find()) {
           // System.out.println(matcher.group());
            String group = matcher.group();
            String[] indyGroup = group.split(",");
            int z = 0;
            for(String line: indyGroup){
            	String newLine = line.replace("#"+y+z, "");
            	readContainer.add(newLine);
            	z++;
            }
            y++;
        }
        String[] readList = new String[readContainer.size()];
        readList = readContainer.toArray(readList);
    	QuantumDataManager.creationContainer.add(readList);
    	if(reissue){
    		QuantumCreatorList.listAdder(readList);
    	}
	}
}
