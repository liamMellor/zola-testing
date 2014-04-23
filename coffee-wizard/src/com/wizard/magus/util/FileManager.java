package com.wizard.magus.util;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.channels.FileChannel;

public class FileManager 
{
	public static File targetDir;
	public static String sudo;
	
	public static boolean saveFile( File folder, String fileName, String jython )
	{
		FileOutputStream f = null;
		File file = new File( folder + File.separator + fileName );
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
	
	public static boolean willOverwrite( File folder, String fileName )
    {
        for( final File fileEntry : folder.listFiles() )
        {
        	if( fileEntry.getName().equals( fileName ) )
        		return true;
        }
        return false;
    }
	
	public static String inputStreamToString( InputStream is ) throws IOException
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
		
		return outString;
	}
	
	
	public static boolean createDir( File file )
	{
		boolean b = file.mkdirs();
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
