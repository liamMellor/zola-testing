package quantum;

import java.awt.BorderLayout;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.BorderFactory;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JTextPane;
import javax.swing.text.BadLocationException;
import javax.swing.text.Style;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyleContext;
import javax.swing.text.StyledDocument;

public class QuantumManagerRightPanel {
	protected static final String buttonString = "JButton";
	JPanel rightSide;
	private JTextPane editorPane;
	private boolean flagOne = true;
	private boolean flagDocActive = false;
	private String newline = "\n";
	private JPanel rightPane;
	private QuantumManagerMain qMain;
	private boolean flagRunActive;

	public QuantumManagerRightPanel(JPanel rightPane, QuantumManagerMain quantumMain){
		this.rightPane = rightPane;
		this.qMain = quantumMain;
		
	}
	public JPanel createRightPane(){
    	final Dimension x = new Dimension(300, 10);
    	final JButton docButton = new JButton("Instructions");
    	docButton.setPreferredSize(x);
        final JButton runButton = new JButton("Run Options");
        //final JButton saveButton = new JButton("Save");
        final JButton creatorButton = new JButton("Creator");
        final JButton homeButton = new JButton("Home");
        final JButton creditsButton = new JButton("Credits");
        final JPanel topBar = new JPanel();
        topBar.add(Box.createRigidArea(new Dimension(100,50)));
        topBar.setLayout(new BoxLayout(topBar, BoxLayout.Y_AXIS));
        topBar.setBorder(BorderFactory.createEmptyBorder(3, 5, 3, 5));
        topBar.add(docButton);
        topBar.add(Box.createVerticalStrut(5));
        topBar.add(runButton);
        //topBar.add(Box.createVerticalStrut(5));
        //topBar.add(saveButton);
        topBar.add(Box.createVerticalStrut(400));
        topBar.add(creatorButton);
        topBar.add(Box.createVerticalStrut(5));
        topBar.add(homeButton);
        topBar.add(Box.createVerticalStrut(5));
        topBar.add(creditsButton);
        QuantumStyleManager.buttonStyles(docButton, runButton, creatorButton, homeButton, creditsButton);
        editorPane = docTextPane();
        final JScrollPane paneScrollPane = new JScrollPane(editorPane);
        paneScrollPane.setVerticalScrollBarPolicy(
                        JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        ActionListener docAL = new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
            	if (!flagDocActive){
	            	qMain.remove(rightPane);
	            	qMain.invalidate();
	            	//repaint();
	            	JSplitPane rightSide;
	                topBar.setLayout(new BoxLayout(topBar, BoxLayout.X_AXIS));
	                topBar.removeAll();
	                docButton.setSelected(true);
	                topBar.add(docButton);
	                topBar.setMaximumSize(new Dimension(0,0));
	            	rightSide = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
	    	        		topBar,
	    	        		paneScrollPane);
	                rightPane = new JPanel(new GridLayout(1,0));
	            	//rightPaneSetter = createRightPane();
	            	rightPane.setBorder(BorderFactory.createCompoundBorder(
	                        BorderFactory.createTitledBorder("Options"),
	                        BorderFactory.createEmptyBorder(5,5,5,5)));
	                rightPane.add(rightSide);
	                rightPane.setPreferredSize(new Dimension(400, 400));
	                qMain.add(rightPane, BorderLayout.LINE_END);
	                qMain.validate();
	                qMain.repaint();
	                flagDocActive = true;
            	}
            	else{
            		qMain.remove(rightPane);
            		qMain.invalidate();
	            	//repaint();
	                topBar.removeAll();
	                topBar.add(Box.createRigidArea(new Dimension(100,50)));
	                topBar.setLayout(new BoxLayout(topBar, BoxLayout.Y_AXIS));
	                topBar.setBorder(BorderFactory.createEmptyBorder(3, 5, 3, 5));
	                topBar.add(docButton);
	                docButton.setSelected(false);
	                topBar.add(Box.createVerticalStrut(5));
	                topBar.add(runButton);
	                topBar.add(Box.createVerticalStrut(400));
	                topBar.add(creatorButton);
	                topBar.add(Box.createVerticalStrut(5));
	                topBar.add(homeButton);
	                topBar.add(Box.createVerticalStrut(5));
	                topBar.add(creditsButton);

	                topBar.setMaximumSize(new Dimension(0,0));
	                rightPane = new JPanel(new GridLayout(1,0));
	            	//rightPaneSetter = createRightPane();
	            	rightPane.setBorder(BorderFactory.createCompoundBorder(
	                        BorderFactory.createTitledBorder("Options"),
	                        BorderFactory.createEmptyBorder(5,5,5,5)));
	                rightPane = topBar;
	                qMain.add(rightPane, BorderLayout.LINE_END);
	                qMain.validate();
	                qMain.repaint();
	                flagDocActive = false;
            	}
            }
        };
        docButton.addActionListener(docAL);
        ActionListener runAL = new ActionListener() {


			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				if (!flagRunActive){
	            	qMain.remove(rightPane);
	            	qMain.invalidate();
	            	//repaint();
	            	JSplitPane rightSide;
	                topBar.setLayout(new BoxLayout(topBar, BoxLayout.X_AXIS));
	                topBar.removeAll();
	                runButton.setSelected(true);
	                topBar.add(runButton);
	                topBar.setMaximumSize(new Dimension(0,0));
	                final JTextField baseUrl = new JTextField(10);
	                baseUrl.setActionCommand("Base URL");
	                JLabel textFieldLabel = new JLabel("Base URL" + ": ");
	                textFieldLabel.setLabelFor(baseUrl);
	                
	            	JPanel textControlsPane = new JPanel();
	                GridBagLayout gridbag = new GridBagLayout();
	                textControlsPane.setBorder(
	                        BorderFactory.createCompoundBorder(
	                                        BorderFactory.createTitledBorder("Runner Options"),
	                                        BorderFactory.createEmptyBorder(5,5,5,5)));
	                textControlsPane.setLayout(gridbag);
	                GridBagConstraints gbc = new GridBagConstraints();
	                gbc.anchor = GridBagConstraints.EAST;
	                gbc.gridwidth = GridBagConstraints.RELATIVE; //next-to-last
	                gbc.fill = GridBagConstraints.NONE;      //reset to default
	                gbc.weightx = 0.0;
	                JButton run = new JButton("Run");
	                textControlsPane.add(textFieldLabel, gbc);
	            	textControlsPane.add(baseUrl, gbc);
	            	textControlsPane.add(run, gbc);
	            	
	            	final JSplitPane textFieldSplit = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
	    	        		topBar,
	    	        		textControlsPane);
	            	final JTextArea runnerConsole = consolePane();
	                final JScrollPane consolePane = new JScrollPane(runnerConsole);
	                consolePane.setVerticalScrollBarPolicy(
	                                JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
	                consolePane.setPreferredSize(new Dimension(250,250));
	                run.addActionListener(new ActionListener(){

						@Override
						public void actionPerformed(ActionEvent e) {
							// TODO Auto-generated method stub
							QuantumDataManager.baseClassURL = baseUrl.getText().toString();
							QuantumRunner.run();
							runnerConsole.append(QuantumDataManager.runnerConsole);
						}
	                	
	                });
	            	JSplitPane topRight = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
	            			textFieldSplit,
	            			consolePane);
	                JButton save = new JButton("SAVE");
	                save.addActionListener(new ActionListener(){
	                	
						@Override
						public void actionPerformed(ActionEvent e) {
							QuantumDataManager.baseClassURL = baseUrl.getText().toString();
							Icon icon = createImageIcon("images/GladosPotato.png", "GLaDOS Potato");
							Object[] possibilities = null;
							// TODO Auto-generated method stub
							String fileName = (String) JOptionPane.showInputDialog(null,
									"What would "
											+ "you like to name this file?",
									"Run and Save",
									JOptionPane.PLAIN_MESSAGE,
									icon,
									possibilities,
									null);
							QuantumDataManager.className = fileName;
							QuantumRunner.compile();
						}
	                	
	                });
	                JButton delete = new JButton("DELETE");
	                JPanel fileControlsPane = new JPanel();
	                GridBagLayout filegridbag = new GridBagLayout();
	                fileControlsPane.setBorder(
	                        BorderFactory.createCompoundBorder(
	                                        BorderFactory.createTitledBorder("Test Options"),
	                                        BorderFactory.createEmptyBorder(5,5,5,5)));
	                fileControlsPane.setLayout(filegridbag);
	                GridBagConstraints filegbc = new GridBagConstraints();
	                filegbc.anchor = GridBagConstraints.EAST;
	                filegbc.gridwidth = GridBagConstraints.RELATIVE; //next-to-last
	                filegbc.fill = GridBagConstraints.NONE;      //reset to default
	                filegbc.weightx = 0.0;
	                fileControlsPane.add(save, gbc);
	                fileControlsPane.add(delete, gbc);
	                fileControlsPane.setPreferredSize(new Dimension(100,100));
	                //baseUrl.addActionListener(this);
	            	rightSide = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
	            			topRight,
	    	        		fileControlsPane);
	                rightPane = new JPanel(new GridLayout(1,0));
	            	//rightPaneSetter = createRightPane();
	            	rightPane.setBorder(BorderFactory.createCompoundBorder(
	                        BorderFactory.createTitledBorder("Runner Options"),
	                        BorderFactory.createEmptyBorder(5,5,5,5)));
	                rightPane.add(rightSide);
	                rightPane.setPreferredSize(new Dimension(400, 400));
	                qMain.add(rightPane, BorderLayout.LINE_END);
	                qMain.validate();
	                qMain.repaint();
	                flagRunActive = true;
            	}
            	else{
            		qMain.remove(rightPane);
            		qMain.invalidate();
	            	//repaint();
	                topBar.removeAll();
	                topBar.add(Box.createRigidArea(new Dimension(100,50)));
	                topBar.setLayout(new BoxLayout(topBar, BoxLayout.Y_AXIS));
	                topBar.setBorder(BorderFactory.createEmptyBorder(3, 5, 3, 5));
	                topBar.add(docButton);
	                docButton.setSelected(false);
	                topBar.add(Box.createVerticalStrut(5));
	                topBar.add(runButton);
	                topBar.add(Box.createVerticalStrut(400));
	                topBar.add(creatorButton);
	                topBar.add(Box.createVerticalStrut(5));
	                topBar.add(homeButton);
	                topBar.add(Box.createVerticalStrut(5));
	                topBar.add(creditsButton);
	                topBar.setMaximumSize(new Dimension(0,0));
	                rightPane = new JPanel(new GridLayout(1,0));
	            	//rightPaneSetter = createRightPane();
	            	rightPane.setBorder(BorderFactory.createCompoundBorder(
	                        BorderFactory.createTitledBorder("Options"),
	                        BorderFactory.createEmptyBorder(5,5,5,5)));
	                rightPane = topBar;
	                qMain.add(rightPane, BorderLayout.LINE_END);
	                qMain.validate();
	                qMain.repaint();
	                flagRunActive = false;
            	}
			}
        };
        runButton.addActionListener(runAL);
        
        if (flagOne){
	        rightSide = topBar;
	        flagOne = false;
        }
		return rightSide;   	
    }
	private JTextArea consolePane() {
		JTextArea textArea = new JTextArea(
                QuantumDataManager.runnerConsole
        );
        textArea.setFont(new Font("Serif", Font.ITALIC, 16));
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);
        JScrollPane areaScrollPane = new JScrollPane(textArea);
        areaScrollPane.setVerticalScrollBarPolicy(
                        JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        areaScrollPane.setPreferredSize(new Dimension(250, 250));
        areaScrollPane.setBorder(
            BorderFactory.createCompoundBorder(
                BorderFactory.createCompoundBorder(
                                BorderFactory.createTitledBorder("Console"),
                                BorderFactory.createEmptyBorder(5,5,5,5)),
                areaScrollPane.getBorder()));
	    return textArea;
    }
	 private JTextPane docTextPane() {
	    	String[] initString =
	            { 
				newline,
				"Welcome test subje-- I mean, valued employee."
	        		+newline+" I hope you are having a good day. "
	        		+newline+"If not, cake and grief counseling will be available at the conclusion of the test."
	        		+newline+" ",
	              newline+"If this is your first time using this service, please read the documentation.",
	              newline+"The writer is simple. Grab the id, or class name, from the respective ",
	              newline+"HTML element, and simply add it here and tell me what action you would like "
	              ,newline+"to take on it.",
	              newline+"In standard HTML formatting, a tag would be represented as so:",
	              newline+"<a href='/dummyURL' id='thisUrl' class='thisClass'> Click Here! </a>",
	              newline+"'a' refers to an anchor tag. This is a clickable button (generally)",
	              newline+"href is a hypertext reference. The characters following are generally the "
	              ,newline+ "link to a URL or web address",
	              newline+"id is the (hopefully) unique identifier for the tag. This will be "
	              ,newline+ "your go-to identifier for creating these Selenium scripts.",
	              newline+"class is the CSS class. this is also targetable by selenium in the "
	              ,newline+ "event that an id is not available",
	              newline+"'Click Here!' is the inner HTML of the tag. This is what"
	              ,newline+ " is displayed to the user.",
	              newline+"'</a>' is the closing tag. This tells the HTML "
	              ,newline+ "interpreter (aka a webpage) that the tag is done.",
	              newline+"There are many tag types in HTML. All of these tags have some "
	              ,newline+ "kind of unique identifer. It is your job to find this unique identifiers.",
	              newline,
	              newline+"It is my job to do the rest.",
	              newline+"...",
	              newline+"Please note that we have added a consequence for failure.",
	              newline+"Any bad data entered will result in an unsatisfactory "
	              ,newline+ "mark on your official testing record, followed by death.",
	              newline,
	              newline+"I am now going to prompt you for two different URL types.",
	              newline+"The first one is the end of the URL. This is the specific page.",
	              newline+"If your URL was http://yahoo.com/signup , you would only enter /signup.",
	              newline+"If you are on the homepage of the website and there is no '/' , enter /index.",
	              newline,
	              newline+"Then I will prompt you for the base URL. This is the "
	              ,newline+ "https:// ... whatever. With no slash at the end."
	             };
		    ArrayList<String> initStyleList = new ArrayList<String>();
		    for(int i = 0; i < initString.length; i++){
		    	if( i == 0 ){
		    		initStyleList.add("icon");
		    	}
		    	else{
		    		initStyleList.add("regular");
		    	}
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
		    textPane.setPreferredSize(new Dimension(100, 100));
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
	        StyleConstants.setComponent(s, button);
	    }
	 protected static ImageIcon createImageIcon(String path,String description) {
		java.net.URL imgURL = QuantumCreatorMain.class.getResource(path);
		if (imgURL != null) {
		return new ImageIcon(imgURL, description);
		} else {
		System.err.println("Couldn't find file: " + path);
		return null;
		}
	 }
}
