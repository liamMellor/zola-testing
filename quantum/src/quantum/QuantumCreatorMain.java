/*
 * Copyright (c) 1995, 2008, Oracle and/or its affiliates. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *   - Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   - Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 *   - Neither the name of Oracle or the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
 * IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */ 

package quantum;


import java.awt.BorderLayout;              //for layout managers and more
import java.awt.Color;
import java.awt.Component;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;        //for action events
import java.awt.event.KeyEvent;
import java.util.Properties;

import javafx.embed.swing.JFXPanel;

import javax.swing.BorderFactory;
import javax.swing.Box;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;
import javax.swing.border.TitledBorder;
import javax.swing.text.Style;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyleContext;
import javax.swing.text.StyledDocument;

import com.jtattoo.plaf.smart.SmartLookAndFeel;

public class QuantumCreatorMain extends JPanel implements ActionListener {
    /**
	 * 
	 */
	private static final long serialVersionUID = 3413241423943899492L;
    protected static final String textFieldString = "Tag Name";
    protected static final String passwordFieldString = "Identifier Type";
    protected static final String ftfString = "Identifier";
    protected static final String actionString = "Action";
    protected static final String sendKeysString = "Keys to send";
    protected static final String buttonString = "JButton";
	private JPanel rightPane;
	private JPanel leftPane;
	private JPanel centerPane;
	private JSplitPane centerSplit;
	private JSplitPane webPage;
	private JSplitPane cPane;
	private static QuantumManagerMain qmMain = new QuantumManagerMain();
	private QuantumCreatorWebView mWebView = new QuantumCreatorWebView();
	public static JTextArea terminal;
	private static QuantumCreatorMain qcMain;

    public QuantumCreatorMain() {
    	QuantumCreatorMain.qcMain = this;
        setLayout(new BorderLayout());

        //Put the editor pane and the text pane in a split pane.
        rightPane = new JPanel(new GridLayout(1,0));
        QuantumCreatorRightPanel quantumRightPanel = new QuantumCreatorRightPanel(rightPane, this);
        rightPane.add(quantumRightPanel.createRightPane());
        rightPane.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createTitledBorder(rightPane.getBorder(),"Options",TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
                        BorderFactory.createEmptyBorder(5,5,5,5)));
        /*
         * 
         */
        webPage = createWebPagePane();
        //JScrollPane webPagePane = new JScrollPane(webPage);
        webPage.setPreferredSize(new Dimension(500, 500));
        webPage.setMinimumSize(new Dimension(400, 400));
        
        centerPane = new JPanel(new GridLayout(1,0));
        JMenuBar menuBar;
    	menuBar = new JMenuBar();
    	
        JButton bKit = new JButton("Browser Kit");
        JButton console = new JButton("Console");
    	QuantumStyleManager.buttonStyles(bKit, console);
        bKit.setForeground(Color.black);
        console.setForeground(Color.black);
        console.addActionListener(new ConsoleButtonListener());
        bKit.addActionListener(new BrowserButtonListener());
    	menuBar.setBackground(Color.red);

        menuBar.add(bKit);
        menuBar.add(console);
        bKit.setPreferredSize(new Dimension(512,30));
        bKit.setMinimumSize(new Dimension(512,30));
        bKit.setSize(new Dimension(512,30));
        console.setPreferredSize(new Dimension(512,30));
        console.setMinimumSize(new Dimension(512,30));
        console.setSize(new Dimension(512,30));
        menuBar.setPreferredSize(new Dimension(1024,30));
        menuBar.setMinimumSize(new Dimension(1024,30));
        menuBar.setSize(new Dimension(1024,30));
        JPanel menuPane = new JPanel();
        menuPane.add(menuBar);
        centerSplit = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        menuPane,
        webPage);
    	centerPane.add(centerSplit);
        centerPane.setPreferredSize(new Dimension(1024,700));
        /*centerPane.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createTitledBorder(getBorder(),"Browser Kit",TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
                        BorderFactory.createEmptyBorder(5,5,5,5)));*/
        /*
         * 
         */
        //Put everything together.
        QuantumCreatorLeftPanel qcLeft = new QuantumCreatorLeftPanel();
        leftPane = new JPanel(new GridLayout(1,0));
        leftPane.add(qcLeft.leftPanel());
        add(leftPane, BorderLayout.LINE_START);
        add(centerPane, BorderLayout.CENTER);
        //add(rightPane, BorderLayout.LINE_END);
    }

    
    private JSplitPane createWebPagePane() {
    	JFXPanel webPagePane = mWebView.initComponents();
        webPagePane.setPreferredSize(new Dimension(1000, 700));
        webPagePane.setMinimumSize(new Dimension(1000, 700));
	    JButton btnGo = new JButton("Go");
	    final JTextField txtURL = new JTextField();
	    JProgressBar progressBar = new JProgressBar();
        ActionListener al = new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
            	QuantumDataManager.currentUrl = txtURL.getText();
                mWebView.loadURL(txtURL.getText());
            }
        };
        QuantumStyleManager.buttonStyles(btnGo);
        btnGo.addActionListener(al);
        txtURL.addActionListener(al);

        progressBar.setPreferredSize(new Dimension(150, 18));
        progressBar.setStringPainted(true);

        JPanel topBar = new JPanel(new BorderLayout(5, 0));
        topBar.setBorder(BorderFactory.createEmptyBorder(3, 5, 3, 5));
        topBar.add(txtURL, BorderLayout.CENTER);
        topBar.add(btnGo, BorderLayout.EAST);
        //topBar.setPreferredSize(new Dimension(5,10));
        topBar.setSize(new Dimension(5, 10));
        JSplitPane webPageTopBar = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        		topBar,
        		webPagePane);
        QuantumDataManager.currentUrl = "http://www.bookish.com";
        mWebView.loadURL("http://www.bookish.com");
        cPane = consolePane();
        return webPageTopBar;
    }
    class ConsoleButtonListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			centerSplit.remove(webPage);
			centerSplit.add(cPane);
			centerSplit.invalidate();
			centerSplit.repaint();
			centerSplit.validate();
		}
    	
    }
    class BrowserButtonListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			centerSplit.remove(cPane);
			webPage.removeAll();
			mWebView.destroy();
			webPage = createWebPagePane();
			centerSplit.add(webPage);
			centerSplit.invalidate();
			centerSplit.repaint();
			centerSplit.validate();
		}
    	
    }
    private JSplitPane consolePane() {
		terminal = new JTextArea(
                QuantumDataManager.runnerConsole
        );
		terminal.setPreferredSize(new Dimension(1024, 500));
		terminal.setMinimumSize(new Dimension(1024, 500));
		terminal.setSize(new Dimension(1024, 500));
		terminal.setFont(new Font("Monospaced", Font.PLAIN, 16));
		terminal.setLineWrap(true);
		terminal.setWrapStyleWord(true);
        JScrollPane areaScrollPane = new JScrollPane(terminal);
        areaScrollPane.setVerticalScrollBarPolicy(
                        JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        areaScrollPane.setPreferredSize(new Dimension(1024, 700));
        areaScrollPane.setMinimumSize(new Dimension(1024, 700));
        areaScrollPane.setSize(new Dimension(1024, 700));

        JPanel miniPane = new JPanel();
        JButton deleteAllSteps = new JButton("Delete All Steps");
        JButton saveAndSubmit = new JButton("Save and Submit");
        saveAndSubmit.addActionListener(new ActionListener(){
        	
			@Override
			public void actionPerformed(ActionEvent e) {
				Icon icon = createImageIcon("images/GladosPotato.png", "GLaDOS Potato");
				Object[] possibilities = null;
				// TODO Auto-generated method stub
				String fileName = (String) JOptionPane.showInputDialog(null,
						"What would "
								+ "you like to name this file?",
						"Save",
						JOptionPane.PLAIN_MESSAGE,
						icon,
						possibilities,
						null);
				QuantumDataManager.className = fileName;
				QuantumRunner.compile();
			}
        	
        });
        QuantumStyleManager.buttonStyles(deleteAllSteps, saveAndSubmit);
        deleteAllSteps.setSize(new Dimension( 300, 200));
        miniPane.add(Box.createVerticalStrut(100));
        miniPane.add(deleteAllSteps);
        miniPane.add(Box.createHorizontalStrut(500));
        miniPane.add(saveAndSubmit);
        miniPane.setPreferredSize(new Dimension(1024, 30));
        miniPane.setMinimumSize(new Dimension(1024, 30));
        miniPane.setSize(new Dimension(1024, 30));
        JSplitPane cFinal = new JSplitPane(JSplitPane.VERTICAL_SPLIT, 
        		terminal, miniPane);
	    return cFinal;
    }
   
    
    public void addStylesToDocument(StyledDocument doc) {
        //Initialize some styles.
        Style def = StyleContext.getDefaultStyleContext().
                        getStyle(StyleContext.DEFAULT_STYLE);

        Style regular = doc.addStyle("regular", def);
        StyleConstants.setFontFamily(def, "SansSerif");

        Style s = doc.addStyle("italic", regular);
        StyleConstants.setItalic(s, true);

        s = doc.addStyle("bold", regular);
        StyleConstants.setBold(s, true);

        s = doc.addStyle("small", regular);
        StyleConstants.setFontSize(s, 10);

        s = doc.addStyle("large", regular);
        StyleConstants.setFontSize(s, 16);

        s = doc.addStyle("icon", regular);
        StyleConstants.setAlignment(s, StyleConstants.ALIGN_CENTER);
        ImageIcon pigIcon = createImageIcon("images/Glados.png",
                                            "GLaDOS");
        if (pigIcon != null) {
            StyleConstants.setIcon(s, pigIcon);
        }

        s = doc.addStyle("button", regular);
        StyleConstants.setAlignment(s, StyleConstants.ALIGN_CENTER);
        ImageIcon soundIcon = createImageIcon("images/iphone_about_abandon.png",
                                              "Abandon");
        JButton button = new JButton();
        if (soundIcon != null) {
            button.setIcon(soundIcon);
        } else {
            button.setText("Abandon");
        }
        button.setCursor(Cursor.getDefaultCursor());
        button.setMargin(new Insets(0,0,0,0));
        button.setActionCommand(buttonString);
        button.addActionListener(this);
        StyleConstants.setComponent(s, button);
    }
    /** Returns an ImageIcon, or null if the path was invalid. */
    protected static ImageIcon createImageIcon(String path,
                                               String description) {
        java.net.URL imgURL = QuantumCreatorMain.class.getResource(path);
        if (imgURL != null) {
            return new ImageIcon(imgURL, description);
        } else {
            System.err.println("Couldn't find file: " + path);
            return null;
        }
    }

    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event dispatch thread.
     */
    static void createAndShowGUI(Component quantumManager) {
        //Create and set up the window.
    	//Create the menu bar.
    	JMenuBar menuBar;
    	JMenu menu;
    	JMenuItem menuItem;
    	menuBar = new JMenuBar();

    	//Build the first menu.
    	menu = new JMenu("Menu");
    	menu.setMnemonic(KeyEvent.VK_A);
    	menu.getAccessibleContext().setAccessibleDescription(
    	        "The only menu in this program that has menu items");
    	menuBar.add(menu);

    	JMenuItem menuItemManager = new JMenuItem("Manager");
    	ActionListener managerAL = new ActionListener(){

			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				
				SwingUtilities.invokeLater(new Runnable() {
		            public void run() {
		            	//if(!QuantumDataManager.managerActive){
		            		QuantumManagerMain.createAndShowGUI(qcMain);
		            		QuantumDataManager.managerActive = true;
		            	//}
		            }
				});
			}
        	
        };
        menuItemManager.addActionListener(managerAL);
        menuItemManager.setMnemonic(KeyEvent.VK_B);
    	menu.add(menuItemManager);
    	
    	//a group of radio button menu items
    	menu.addSeparator();
    	menuItem = new JMenuItem("Help");
    	menuItem.setMnemonic(KeyEvent.VK_R);
    	menu.add(menuItem);
    	
    	menu.addSeparator();
    	menuItem = new JMenuItem("Credits");
    	menuItem.setMnemonic(KeyEvent.VK_R);
    	menu.add(menuItem);
    	
    	JButton Site = new JButton("     Site     ");
    	
    	JButton API = new JButton("     API      ");
    	API.addActionListener(new ActionListener(){
    		
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				APIshCreatorMain.createAndShowGUI(qcMain);
			}
    		
    	});
    	QuantumStyleManager.buttonStyles(Site, API);
    	Site.setForeground(Color.black);
    	API.setForeground(Color.black);
    	
    	menu.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createEmptyBorder(10,10,10,10), BorderFactory.createLineBorder(Color.black, 1)));
    	menuBar.add(Site);
    	menuBar.add(API);
    	
    	QuantumDataManager.frame.setJMenuBar(menuBar);
        QuantumDataManager.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        if(quantumManager != null){
        	QuantumDataManager.frame.remove(quantumManager);
        }
        
        //Add content to the window.
        QuantumDataManager.frame.add(new QuantumCreatorMain());
        //Display the window.
        
        QuantumDataManager.frame.pack();
        QuantumDataManager.frame.setFont(QuantumStyleManager.mightyFont());
        QuantumDataManager.frame.setVisible(true);
    }

    public static void main(String[] args) throws ClassNotFoundException, InstantiationException, IllegalAccessException, UnsupportedLookAndFeelException {
        //Schedule a job for the event dispatching thread:
        //creating and showing this application's GUI.
    	 // Create a property object 
    	//URL imgUrl = QuantumCreatorMain.class.getClass().getResource("images/GladosPotato.png");
        
    	
    	Properties props = new Properties();
    	props.put("logoString", "Quantum");
        props.put("selectionBackgroundColor", "220 208 255"); 
        props.put("menuSelectionBackgroundColor", "220 208 255"); 
        
        props.put("controlColor", "218 254 230");
        props.put("controlColorLight", "218 254 230");
        props.put("controlColorDark", "180 240 197"); 

        props.put("buttonColor", "218 230 254");
        props.put("buttonColorLight", "255 255 255");
        props.put("buttonColorDark", "244 242 232");

        props.put("rolloverColor", "218 254 230"); 
        props.put("rolloverColorLight", "218 254 230"); 
        props.put("rolloverColorDark", "180 240 197"); 

        props.put("windowTitleForegroundColor", "255 255 255");
        props.put("windowTitleBackgroundColor", "102 0 153"); 
        props.put("windowTitleColorLight", "220 208 255"); 
        props.put("windowTitleColorDark", "103 30 49"); 
        props.put("windowBorderColor", "0 0 0");
        SmartLookAndFeel.setCurrentTheme(props);
        UIManager.setLookAndFeel("com.jtattoo.plaf.smart.SmartLookAndFeel");
       /* Properties props = new Properties();
        // This property switches the layout style of the scrollbars.
        props.put("linuxStyleScrollBar", "on");
        // Set the theme
        com.jtattoo.plaf.acryl.AcrylLookAndFeel.setCurrentTheme(props);*/
        
        // Select the Look and Feel
       // UIManager.setLookAndFeel("com.jtattoo.plaf.acryl.AcrylLookAndFeel");
        
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                
				createAndShowGUI(qmMain);

            }
        });
    }
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
	}
}
