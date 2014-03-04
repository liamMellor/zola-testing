package src.quantum;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

import org.apache.http.client.ClientProtocolException;
import org.json.JSONException;
import org.json.JSONObject;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

public class APIshRunner {
	//private static String everything;
	public static void run() {
		for(int i = 0; i < APIshDataManager.urlUp.size(); i++){
			try {
				JSONObject result = APIshTestTemplate.apiRequest(i);
				Gson gson = new GsonBuilder().setPrettyPrinting().create();
				JsonParser jp = new JsonParser();
				JsonElement je = jp.parse(result.toString());
				String prettyJsonString = gson.toJson(je);
				APIshCreatorMain.terminal.append(prettyJsonString);

			}
			 catch (ClientProtocolException e) {
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
