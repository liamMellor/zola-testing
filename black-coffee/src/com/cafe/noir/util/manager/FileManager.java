package com.cafe.noir.util.manager;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.channels.FileChannel;
import java.util.ArrayList;

import javafx.scene.control.TabPane;
import javafx.scene.control.TreeView;
import javafx.scene.web.WebView;

import com.cafe.noir.directeur.DirecteurLeftPanel;
import com.cafe.noir.panels.listeners.OnRunListener;

public class FileManager 
{
	public static boolean saveFile( File folder, String fileName, String jython )
	{
		FileOutputStream f = null;
		File file = new File( folder + File.separator + fileName + ".py" );
		try
		{
			f = new FileOutputStream( file );
			f.write( jython.getBytes() );
			
			f.flush();
			f.close();	    
		}
		catch ( IOException e ) 
	    {
			e.printStackTrace();
		} 
		
		return file.exists();
	}
	
	public static ArrayList<Boolean> deleteFiles( ArrayList<Boolean> boolList, File... files )
	{
		for( File file : files )
		{
			if( file.isDirectory() )
			{
				boolList.addAll( deleteFiles( new ArrayList<Boolean>(), file.listFiles() ) );
				boolList.add( file.delete() );
			}
			else
			{
				boolList.add( file.delete() );
			}
		}
		return boolList;
	}
	
	public static boolean willOverwrite( File folder, String fileName )
    {
        for( final File fileEntry : folder.listFiles() )
        {
        	if( fileEntry.getName().equals( fileName ) )
        		return true;
        }
        return false;
    }
	
	public static String inputStreamToString( InputStream err, InputStream log ) throws IOException 
	{
	    StringBuilder sb = new StringBuilder();
	    
		sb.append( "<html><body><p style='color:red;font-family:monospace;'>" + inputStreamToString( err, true ) + "</p>" );

	    sb.append( "<p style='color:black;font-family:monospace;'>" + inputStreamToString( log, true ) + "</p></html>" );

	    return sb.toString();
    }
	
	public static String inputStreamToString( InputStream is, boolean toHtml ) throws IOException
	{
		ByteArrayOutputStream out = new ByteArrayOutputStream();
		while( true )
	    {
	    	int c = is.read();
	    	if ( c == -1 ) break;
	    	out.write( (char) c );
	    }
		
		String outString = new String( out.toByteArray() );
		out.flush();
		out.close();
		
		if( toHtml )
		{
			CharSequence newLine = "\n";
			CharSequence lineBreak = "</br>";
			outString = outString.replace( newLine, lineBreak );
		}
		
		return outString;
	}
	
	public static void saveTempScriptAndRun( TabPane tabPane, WebView webView, String fileName, String jython )
	{
		tabPane.getSelectionModel().select( 1 );
		FileOutputStream f = null;
		try
		{
			f = new FileOutputStream( new File( fileName ) );
			f.write( jython.getBytes() );
			
			f.flush();
			f.close();
			
			Runtime rt = Runtime.getRuntime();
			Process p = rt.exec( OnRunListener.PYTHON + " " + fileName );
			p.waitFor();
	    
			webView.getEngine().loadContent( FileManager.inputStreamToString( p.getErrorStream(), p.getInputStream() ) );
		}
		catch (IOException | InterruptedException e1) 
	    {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		} 
	}
	
	public static void runScript( WebView webView, TreeView<File> treeView )
	{
		StringBuilder sb = new StringBuilder();
		for( int i = 0; i < treeView.getChildrenUnmodifiable().size(); i++)
		{
			runScripts( webView, sb, treeView.getTreeItem( i ).getValue() );
		}
	}
	
	public static void runScripts( WebView webView, StringBuilder sb, File... files )
	{
		for( File file : files )
		{
			if( file.isDirectory() )
			{
				runScripts( webView, sb, file.listFiles() );
			}
			else
			{
				try 
				{
					Runtime rt = Runtime.getRuntime();
					Process p = rt.exec( OnRunListener.PYTHON + " " + file );
					p.waitFor();
					sb.append( FileManager.inputStreamToString( p.getErrorStream(), p.getInputStream() ) );
				} 
				catch (InterruptedException | IOException e) 
				{
					e.printStackTrace();
				}
				webView.getEngine().loadContent( sb.toString() );
			}
		}
		
	}
	public static boolean createDir( File file )
	{
		boolean b = file.mkdirs();
		DirecteurLeftPanel.notifyDataSetChanged();
		return b;
	}
	
	public static void copyFile( File sourceFile, File destFile ) throws IOException, FileNotFoundException
	{
		if( sourceFile.isDirectory() )
		{
			destFile.mkdir();
			for( File file : sourceFile.listFiles() )
			{
				copyFile( file, new File( destFile + File.separator + file.getName() ) );
			}
		}
		else
		{
			privCopy( sourceFile, destFile );
		}
	}
	private static void privCopy( File sourceFile, File destFile ) throws IOException, FileNotFoundException
	{
		if( !destFile.exists() ) 
	    {
	        destFile.createNewFile();
	    }

	    FileChannel source = null;
	    FileChannel destination = null;

	    try 
	    {
	        source = new FileInputStream( sourceFile ).getChannel();
	        destination = new FileOutputStream( destFile ).getChannel();
	        destination.transferFrom( source, 0, source.size() );
	    }
	    finally 
	    {
	        if( source != null ) 
	        {
	            source.close();
	        }
	        if( destination != null ) 
	        {
	            destination.close();
	        }
	    }
	}
}
