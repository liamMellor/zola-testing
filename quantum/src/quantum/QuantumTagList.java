package quantum;

import java.io.IOException;
import java.util.ArrayList;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class QuantumTagList {
	public static String[] tagList(){
		String[] tagList = {"html",
		                    "title","body" ,"h1" ,
		                    "h2" ,"h3" ,"h4",
		                    "h5" ,"h6" ,"p" ,
		                    "br" ,"hr" ,"form" ,
		                    "input" ,"button" ,"textarea" ,
		                    "button" ,"select" ,"optgroup" ,
		                    "option","label" ,"iframe" ,
		                    "img" ,"area" ,"a" ,
		                    "link" ,"nav" ,"ul" 
		                    ,"ol" ,"li" ,"dl",
		                    "menu" ,"table" ,"th" 
		                    ,"tr" ,"td" ,"thead" 
		                    ,"tbody" ,"tfoot" 
		                    ,"col" ,"colgroup" 
		                    ,"style" ,"div" ,"span" ,
		                    "header" ,"footer" ,"section" ,
		                    "article" ,"head" ,"meta" ,"base"};
		return tagList;
	}
	public String[] parser(String url, String tag){
		Document doc = null;
		try {
			doc = Jsoup.connect(url).get();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    Elements tags = doc.select(tag);
	    ArrayList<String> elementList = new ArrayList<String>();
	    for(Element thisTag: tags){
	    	elementList.add(thisTag.toString());
	    }
	    String[] elementArray = new String[elementList.size()];
	    elementArray = elementList.toArray(elementArray);
	    return elementArray;
	}
}
