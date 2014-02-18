package quantum;

import java.util.ArrayList;


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
}
