package com.cafe.noir;

import javafx.scene.control.SplitPane;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.control.TabPane.TabClosingPolicy;
import javafx.scene.layout.Pane;
import javafx.scene.web.WebView;

import com.cafe.noir.avant.AvantLeftPanel;
import com.cafe.noir.panels.TerminalPanel;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.webkit.NoirWebView;

public class AvantViewController extends SplitPane
{
	public static TabPane tabPane;
	public static WebView terminal;

	public AvantViewController()
	{
		super();
		final Pane webPanel = new Pane();
        
        webPanel.getChildren().add( new NoirWebView( "http://bookish.com" ).create() );
        
        tabPane = new TabPane();
        
        Tab browser = new Tab( "Browser" );
        browser.setContent( webPanel );
        
        Tab consoleTab = new Tab( "Console" );
        TerminalPanel terminalPanel = new TerminalPanel( FrameType.Avant );
        consoleTab.setContent( terminalPanel );
        terminal = terminalPanel.getTerminal();
        
        tabPane.getTabs().add( browser );
        tabPane.getTabs().add( consoleTab );
        tabPane.setTabClosingPolicy( TabClosingPolicy.UNAVAILABLE );
        
        AvantLeftPanel avantLeftPanel = new AvantLeftPanel();
        getItems().addAll( avantLeftPanel, tabPane );
	}
}
