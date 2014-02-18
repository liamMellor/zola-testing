package quantum;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.commons.io.IOUtils;
import org.apache.commons.lang3.StringUtils;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class QuantumRunner {
	//private static String everything;
	public static void run(){
		Result result = JUnitCore.runClasses(QuantumTestTemplate.class);
	    for (Failure failure : result.getFailures()){
            System.out.println(failure.toString());
            QuantumDataManager.runnerConsole = failure.toString();
	    }
	}
	public static void compile() {

        File qtmTest = new File("QuantumScripts/epoch/"+QuantumDataManager.className+".qtm");
        if (qtmTest.getParentFile().exists() || qtmTest.getParentFile().mkdirs()) {

            try {
                Writer writer = null;
                try {
                    writer = new FileWriter(qtmTest);
                    writer.write(QuantumConstructor.contruct());
                    writer.flush();
                } finally {
                    try {
                        writer.close();
                    } catch (Exception e) {
                    }
                }
            
	        } catch (IOException exp) {
	            exp.printStackTrace();
	        }
        }
	}
	public static void reconstruct(String everything) {
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
	}
}
