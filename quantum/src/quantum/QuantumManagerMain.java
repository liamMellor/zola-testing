package quantum;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javafx.embed.swing.JFXPanel;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTextField;
import javax.swing.JTextPane;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.text.BadLocationException;
import javax.swing.text.Style;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyleContext;
import javax.swing.text.StyledDocument;

public class QuantumManagerMain extends JPanel implements ActionListener {
    private String newline = "\n";
    protected static final String textFieldString = "Tag Name";
    protected static final String passwordFieldString = "Identifier Type";
    protected static final String ftfString = "Identifier";
    protected static final String actionString = "Action";
    protected static final String sendKeysString = "Keys to send";
    protected static final String buttonString = "JButton";
    private String emptyLine = "\n";
	private JPanel rightPaneSetter;
	private JPanel rightPane;
	private JPanel leftPane;
	private JPanel centerPane;
	private JTextPane tagPage;
	private int creationIterator;
	
    public QuantumManagerMain() {
    	
        setLayout(new BorderLayout());
        //Create a regular text field.
       
        QuantumManagerList qList = new QuantumManagerList();
        final JSplitPane quantumDataList = qList.QuantumList();
        //HireListener hireListener = new HireListener(mSubmit);
        
        QuantumManagerList.list.addListSelectionListener(new ListSelectionListener() {

			@Override
			public void valueChanged(ListSelectionEvent e) {
				// TODO Auto-generated method stub
				//QuantumList.list.setSelectedIndex(QuantumList.listModel.size()-1);
				QuantumManagerList.fireButton.setEnabled(true);
				QuantumManagerList.moveRightButton.setEnabled(true);
				QuantumManagerList.editorButton.setEnabled(true);
			}
        	
        });
        quantumDataList.setBorder(
                BorderFactory.createCompoundBorder(
                                BorderFactory.createTitledBorder("Scripts"),
                                BorderFactory.createEmptyBorder(5,5,5,5)));
        leftPane = new JPanel(new BorderLayout());
        leftPane.add(quantumDataList);

        //Put the editor pane and the text pane in a split pane.
        rightPane = new JPanel(new GridLayout(1,0));
        QuantumManagerRightPanel quantumRightPanel = new QuantumManagerRightPanel(rightPane, this);
        rightPane.add(quantumRightPanel.createRightPane());
        rightPane.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createTitledBorder("Options"),
                        BorderFactory.createEmptyBorder(5,5,5,5)));
        /*
         * 
         */
        final JSplitPane webPage = createWebPagePane();
        //JScrollPane webPagePane = new JScrollPane(webPage);
        webPage.setPreferredSize(new Dimension(500, 500));
        webPage.setMinimumSize(new Dimension(400, 400));

        centerPane = new JPanel(new GridLayout(1,0));
        QuantumManagerCenterPanel quantumCenterPanel = new QuantumManagerCenterPanel(centerPane, this);
        centerPane.add(quantumCenterPanel.QuantumTopCenter());
        centerPane.setBorder(BorderFactory.createCompoundBorder(
                        BorderFactory.createTitledBorder("WebPage"),
                        BorderFactory.createEmptyBorder(5,5,5,5)));
        /*
         * 
         */
        //Put everything together.
        
        
        add(leftPane, BorderLayout.LINE_START);
        add(centerPane, BorderLayout.CENTER);
        add(rightPane, BorderLayout.LINE_END);
    }
    
    private JSplitPane createWebPagePane() {
    	final QuantumCreatorWebView mWebView = new QuantumCreatorWebView();
    	JFXPanel webPagePane = mWebView.initComponents();
        webPagePane.setPreferredSize(new Dimension(500, 700));
        webPagePane.setMinimumSize(new Dimension(500, 700));
	    JButton btnGo = new JButton("Go");
	    final JTextField txtURL = new JTextField();
	    JProgressBar progressBar = new JProgressBar();
        ActionListener al = new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
            	QuantumDataManager.currentUrl = txtURL.getText();
                mWebView.loadURL(txtURL.getText());
            }
        };

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
    public static void createAndShowGUI(QuantumCreatorMain qcMain) {
        //Create and set up the window.
    	QuantumDataManager.frame.setTitle("QuANTUM Manager");
        QuantumDataManager.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add content to the window.
        QuantumDataManager.frame.add(new QuantumManagerMain());
        QuantumDataManager.frame.remove(qcMain);
        //Display the window.
        QuantumDataManager.frame.pack();
        QuantumDataManager.frame.setVisible(true);
    }

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
	}

}
