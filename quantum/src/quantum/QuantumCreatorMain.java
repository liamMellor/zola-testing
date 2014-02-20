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
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;        //for action events
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.Properties;

import javafx.embed.swing.JFXPanel;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTextField;
import javax.swing.JTextPane;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;
import javax.swing.border.TitledBorder;
import javax.swing.text.BadLocationException;
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
	private JComboBox<?> petList;
	private JTextPane tagPage;
	private static QuantumManagerMain qmMain;
	
    public QuantumCreatorMain(QuantumManagerMain qmMain) {
    	QuantumCreatorMain.qmMain = qmMain;
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
        final JSplitPane webPage = createWebPagePane();
        //JScrollPane webPagePane = new JScrollPane(webPage);
        webPage.setPreferredSize(new Dimension(500, 500));
        webPage.setMinimumSize(new Dimension(400, 400));

        //Create a text pane.
        tagPage = createTextPane("html");
        final JScrollPane tagScrollPane = new JScrollPane(tagPage);
        tagScrollPane.setVerticalScrollBarPolicy(
                        JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        tagScrollPane.setPreferredSize(new Dimension(700, 700));
        tagScrollPane.setMinimumSize(new Dimension(700, 700));
        petList = new JComboBox<Object>(QuantumTagList.tagList());
        petList.setSelectedIndex(0);
        petList.setPreferredSize(new Dimension(10, 50));
        petList.setMinimumSize(new Dimension(10, 50));
        JButton btnGo = new JButton("Go");
	    final JTextField txtURL = new JTextField();
	    JPanel webBar = new JPanel(new BorderLayout(5, 0));
	    webBar.setBorder(BorderFactory.createEmptyBorder(3, 5, 3, 5));
	    webBar.add(txtURL, BorderLayout.CENTER);
	    webBar.add(btnGo, BorderLayout.EAST);
        //topBar.setPreferredSize(new Dimension(5,10));
	    webBar.setSize(new Dimension(5, 10));
        final JSplitPane webPageTopBar = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        		webBar,
        		petList);
        ActionListener btnGoAL = new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				QuantumDataManager.currentUrl = txtURL.getText();
				remove(centerPane);
                invalidate();
                repaint();
                centerPane = new JPanel(new GridLayout(1,0));
            	tagPage = createTextPane(petList.getSelectedItem().toString());
            	final JScrollPane tagScrollPane = new JScrollPane(tagPage);
                tagScrollPane.setVerticalScrollBarPolicy(
                                 JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
                tagScrollPane.setPreferredSize(new Dimension(700, 700));
                tagScrollPane.setMinimumSize(new Dimension(700, 700));
            	final JSplitPane splitPane2Inner = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
                		tagScrollPane,
                		webPageTopBar);
            	splitPane2Inner.setOneTouchExpandable(true);
            	splitPane2Inner.setResizeWeight(0.5);
            	centerPane.add(splitPane2Inner);
                centerPane.setBorder(BorderFactory.createCompoundBorder(
                                BorderFactory.createTitledBorder(getBorder(),"Browser Kit",TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
                                BorderFactory.createEmptyBorder(5,5,5,5)));
                add(centerPane);
                validate();
                repaint();
			}
        	
        };
        btnGo.addActionListener(btnGoAL);
        //petList.se
        ActionListener comboBoxAL = new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                remove(centerPane);
                invalidate();
                repaint();
                centerPane = new JPanel(new GridLayout(1,0));
            	tagPage = createTextPane(petList.getSelectedItem().toString());
            	final JScrollPane tagScrollPane = new JScrollPane(tagPage);
                tagScrollPane.setVerticalScrollBarPolicy(
                                 JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
                tagScrollPane.setPreferredSize(new Dimension(700, 700));
                tagScrollPane.setMinimumSize(new Dimension(700, 700));
            	final JSplitPane splitPane2Inner = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
                		tagScrollPane,
                		webPageTopBar);
            	splitPane2Inner.setOneTouchExpandable(true);
            	splitPane2Inner.setResizeWeight(0.5);
            	centerPane.add(splitPane2Inner);
                centerPane.setBorder(BorderFactory.createCompoundBorder(
                                BorderFactory.createTitledBorder(getBorder(),"Browser Kit",TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
                                BorderFactory.createEmptyBorder(5,5,5,5)));
                add(centerPane);
                validate();
                repaint();
            }
        };
        petList.addActionListener(comboBoxAL);
        centerPane = new JPanel(new GridLayout(1,0));
        centerPane.add(webPage);
        centerPane.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createTitledBorder(getBorder(),"Browser Kit",TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
                        BorderFactory.createEmptyBorder(5,5,5,5)));
        /*
         * 
         */
        //Put everything together.
        QuantumCreatorLeftPanel qcLeft = new QuantumCreatorLeftPanel();
        leftPane = new JPanel(new GridLayout(1,0));
        leftPane.add(qcLeft.leftPanel());
        add(leftPane, BorderLayout.LINE_START);
        add(centerPane, BorderLayout.CENTER);
        add(rightPane, BorderLayout.LINE_END);
    }

    public void actionPerformed(ActionEvent e) {
    }
    
    private JSplitPane createWebPagePane() {
    	final QuantumCreatorWebView mWebView = new QuantumCreatorWebView();
    	JFXPanel webPagePane = mWebView.initComponents();
        webPagePane.setPreferredSize(new Dimension(430, 700));
        webPagePane.setMinimumSize(new Dimension(430, 700));
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
        		webPagePane,
        		topBar);
        QuantumDataManager.currentUrl = "http://www.bookish.com";
        mWebView.loadURL("http://www.bookish.com");
        return webPageTopBar;
    }
    
    private JTextPane createTextPane(String selectedItem) {
    	QuantumTagList qtl = new QuantumTagList();
        String[] initString = qtl.parser(QuantumDataManager.currentUrl, selectedItem);
	    ArrayList<String> initStyleList = new ArrayList<String>();

        for(int i = 0; i < initString.length; i++){
    		initStyleList.add("regular");
	    }
        String[] initStyles = new String[initStyleList.size()];
	    initStyles = initStyleList.toArray(initStyles);
        JTextPane textPane = new JTextPane();
        StyledDocument doc = textPane.getStyledDocument();
        addStylesToDocument(doc);

        try {
            for (int i=0; i < initString.length; i++) {
                doc.insertString(doc.getLength(), initString[i],
                                 doc.getStyle(initStyles[i]));
            }
        } catch (BadLocationException ble) {
            System.err.println("Couldn't insert initial text into text pane.");
        }
        textPane.setPreferredSize(new Dimension(700, 700));
        textPane.setMinimumSize(new Dimension(700, 700));
        textPane.setEditable(false);
        return textPane;
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
    static void createAndShowGUI(QuantumManagerMain qmMain) {
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

    	//a group of JMenuItems
    	menuItem = new JMenuItem("Creator",
    	                         KeyEvent.VK_T);
    	menuItem.getAccessibleContext().setAccessibleDescription(
    	        "This doesn't really do anything");
    	menu.add(menuItem);

    	menuItem = new JMenuItem("Manager");
    	menuItem.setMnemonic(KeyEvent.VK_B);
    	menu.add(menuItem);

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
    	
    	QuantumStyleManager.buttonStyles(Site, API);
    	Site.setForeground(Color.black);
    	API.setForeground(Color.black);
    	
    	menu.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createEmptyBorder(10,10,10,10), BorderFactory.createLineBorder(Color.black, 1)));
    	menuBar.add(Site);
    	menuBar.add(API);
    	
    	QuantumDataManager.frame.setJMenuBar(menuBar);
        QuantumDataManager.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        if(qmMain != null){
        	QuantumDataManager.frame.remove(qmMain);
        }
        
        //Add content to the window.
        QuantumDataManager.frame.add(new QuantumCreatorMain(qmMain));
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
}
