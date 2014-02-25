package quantum;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

import javax.swing.Icon;
import javax.swing.filechooser.FileSystemView;

import org.apache.http.client.ClientProtocolException;
import org.json.JSONException;
import org.json.JSONObject;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class APIshRunner {
	//private static String everything;
	public static void run(){
		for(int i = 0; i < APIshDataManager.urlUp.size(); i++){
			try {
				JSONObject result = APIshTestTemplate.apiRequest(i);
				APIshCreatorMain.terminal.append(result.toString());
			} catch (ClientProtocolException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	public static void compile() {

        File apshTest = new File("QuantumScripts/aeon/."+APIshDataManager.className+".api");
        if (apshTest.getParentFile().exists() || apshTest.getParentFile().mkdirs()) {

            try {
                Writer writer = null;
                try {
                    writer = new FileWriter(apshTest);
                    writer.write(APIshConstructor.construct());
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
