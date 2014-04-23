package com.cafe.noir;

import javafx.scene.control.SplitPane;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.layout.Pane;
import javafx.scene.web.WebView;

import com.cafe.noir.arriere.ArriereLeftPanel;
import com.cafe.noir.panels.TerminalPanel;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.webkit.NoirWebView;

public class ArriereViewController extends SplitPane
{
	public static TabPane tabPane;
	public static WebView terminal;

	public ArriereViewController()
	{
		super();
		final Pane webPanel = new Pane();
        webPanel.getChildren().add( new NoirWebView( "http://apiary.io" ).create() );
        
        tabPane = new TabPane();
        Tab browser = new Tab( "Browser" );
        
        browser.setContent( webPanel );
        
        Tab console = new Tab( "Console" );

        TerminalPanel terminalPane = new TerminalPanel( FrameType.Arriere );
        console.setContent( terminalPane );
        terminal = terminalPane.getTerminal();
        
        tabPane.getTabs().add( browser );
        tabPane.getTabs().add( console );
        
        ArriereLeftPanel arriereLeftPanel = new ArriereLeftPanel();
        getItems().addAll( arriereLeftPanel, tabPane );
	}
}
