package com.wizard.magus.util;

import java.io.File;
import java.net.URL;

import javafx.concurrent.Task;
import javafx.scene.control.ProgressBar;

public class Make extends Task<Void>
{
	private ProgressBar progBar;
	
	public Make( ProgressBar pBar )
	{
		this.progBar = pBar;
	}
	
	@Override
	protected Void call() throws Exception 
	{
		progBar.setProgress( 0 );
		
		Runtime rt = Runtime.getRuntime();
		
		File newApp = new File( FileManager.targetDir + File.separator + "Black Coffee.app" );
		newApp.mkdirs();
		
		progBar.setProgress( 10 );
		
		File contents = new File( newApp + File.separator + "Contents" );
		contents.mkdirs();
		
		progBar.setProgress( 20 );

		URL plistUrl = getClass().getResource( "/binaries/Info.plist" );
		File plist = new File( plistUrl.getPath() );
		
		FileManager.copyFile( plist, new File( contents + File.separator + "Info.plist" ) );
		
		progBar.setProgress( 30 );

		File macOS = new File( contents + File.separator + "MacOS" );
		macOS.mkdirs();
		
		URL jarUrl = getClass().getResource( "/binaries/black_coffee.jar" );
		File jarFile = new File( jarUrl.getPath() );
		
		progBar.setProgress( 40 );

		URL launcherUrl = getClass().getResource( "/binaries/launcher" );
		File launcherFile = new File( launcherUrl.getPath() );
		
		progBar.setProgress( 50 );

		FileManager.copyFile( jarFile, new File( macOS + File.separator + "black_coffee.jar" ) );
		
		progBar.setProgress( 60 );

		FileManager.copyFile( launcherFile, new File( macOS + File.separator + "launcher" ) );
		
		progBar.setProgress( 70 );

		File res = new File( contents + File.separator + "Resources" );
		res.mkdirs();
		
		URL icnsUrl = getClass().getResource( "/binaries/application.icns" );
		File icns = new File( icnsUrl.getPath() );
		
		progBar.setProgress( 80 );

		FileManager.copyFile( icns, new File( res + File.separator + "application.icns" ) );
		
		Process p = rt.exec( "$echo " + FileManager.sudo + " | sudo -S easy_install selenium" );
		p.waitFor();
		progBar.setProgress( 90 );

		p = rt.exec( "$echo " + FileManager.sudo + " | sudo -S easy_install urllib" );
		p.waitFor();
		p = rt.exec( "$echo " + FileManager.sudo + " | sudo -S chmod +x " );
		progBar.setProgress( 100 );
		return null;
	}

}
