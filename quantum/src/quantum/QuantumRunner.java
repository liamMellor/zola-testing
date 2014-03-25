package quantum;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

import org.apache.xerces.impl.dv.util.Base64;
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

        File qtmTest = new File("QuantumScripts/epoch/."+QuantumDataManager.className+".qtm");
        qtmTest.setReadOnly();
        if (qtmTest.getParentFile().exists() || qtmTest.getParentFile().mkdirs()) {

            try {
                Writer writer = null;
                try {
                    writer = new FileWriter(qtmTest);
                    String encryptedFile = Base64.encode(QuantumConstructor.construct().getBytes());
                    writer.write(encryptedFile);
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
	
}
