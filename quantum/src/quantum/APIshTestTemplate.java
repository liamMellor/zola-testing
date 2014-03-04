package src.quantum;

import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map.Entry;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;

import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.utils.URLEncodedUtils;
import org.apache.http.conn.scheme.Scheme;
import org.apache.http.conn.scheme.SchemeRegistry;
import org.apache.http.conn.ssl.SSLSocketFactory;
import org.apache.http.conn.ssl.X509HostnameVerifier;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.impl.conn.SingleClientConnManager;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONException;
import org.json.JSONObject;

public class APIshTestTemplate {

	private final static String USER_AGENT = "Mozilla/5.0";
	 
    public static JSONObject apiRequest(int n) throws ClientProtocolException, IOException, JSONException{
         HostnameVerifier hostnameVerifier = org.apache.http.conn.ssl.SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER;
        
         DefaultHttpClient client = new DefaultHttpClient();

         SchemeRegistry registry = new SchemeRegistry();
         SSLSocketFactory socketFactory = SSLSocketFactory.getSocketFactory();
         socketFactory.setHostnameVerifier((X509HostnameVerifier) hostnameVerifier);
         registry.register(new Scheme("https", socketFactory, 443));
         SingleClientConnManager mgr = new SingleClientConnManager(client.getParams(), registry);
         DefaultHttpClient httpClient = new DefaultHttpClient(mgr, client.getParams());

         // Set verifier    
         HttpsURLConnection.setDefaultHostnameVerifier(hostnameVerifier);
         final String url = APIshDataManager.urlUp.get(n);
         
         JSONObject response = null;
         try {
              // Add your data
              List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>();
              LinkedHashMap<String, String> kvps = APIshDataManager.creationContainer.get(n);
              for(Entry<String, String> kvpEntries : kvps.entrySet()){
            	  nameValuePairs.add(new BasicNameValuePair(kvpEntries.getKey(), kvpEntries.getValue()));
              }
              String responseBody;
              if (APIshDataManager.requestType.get(n).equals("POST")){
            	  HttpPost httppost = new HttpPost(url);
	              httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));
	             
	              // Execute HTTP Post Request
	              ResponseHandler<String> responseHandler=new BasicResponseHandler();
	              responseBody = httpClient.execute(httppost, responseHandler);
              }
              else{
            	  String paramString = URLEncodedUtils.format(nameValuePairs, "utf-8");
            	  HttpGet httpget = new HttpGet(url+paramString);
            	  ResponseHandler<String> responseHandler=new BasicResponseHandler();
            	  responseBody = httpClient.execute(httpget, responseHandler);
              }
              response=new JSONObject(responseBody);
         } catch (ClientProtocolException e) {
              // TODO Auto-generated catch block
              System.out.println(e);
         } catch (IOException e) {
              // TODO Auto-generated catch block
              System.out.println(e);
         } catch (JSONException e) {
              // TODO Auto-generated catch block
              e.printStackTrace();
         }
         System.out.println(response);
         return response;
    }
}
