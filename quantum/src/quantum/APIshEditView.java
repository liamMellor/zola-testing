package src.quantum;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import java.util.LinkedHashMap;

import javax.swing.BorderFactory;
import javax.swing.Box;
import javax.swing.DefaultListModel;
import javax.swing.Icon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.JTextField;
import javax.swing.JComponent;
import javax.swing.border.TitledBorder;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import src.quantum.APIshCreatorLeftPanel.MinusListener;
import src.quantum.APIshCreatorLeftPanel.PlusListener;
import src.quantum.APIshCreatorLeftPanel.kvpHinter;


public class APIshEditView extends JPanel{
	
	static JList list;
	static DefaultListModel listModel;

	protected static final String cancelString = "Cancel";
	protected static final String replaceString = "Replace";
	protected static final String urlString = "Base URL";
    protected static final String restCallString = "REST call";
    protected static final String keyString = "Key";
    protected static final String valueString = "Value";
    
    protected static JPanel editPane;
			
	private static JComboBox<Object> restCallType;
	
	private static JTextField urlTextField;
	private static JTextField keysToSend;
	private static JTextField valuesToSend;
	
	private static ArrayList<JComboBox> comboBoxes = new ArrayList<JComboBox>();
	private static ArrayList<JTextField> textFields = new ArrayList<JTextField>();
	private static ArrayList<JLabel> labels = new ArrayList<JLabel>();
	private static ArrayList<Component> compsComp;
	private static ArrayList<JTextField> keysList;
	private static ArrayList<JTextField> valuesList;
	
	private static JLabel restCallLabel;
	private static JLabel urlLabel;
	private static JLabel valuesLabel;
	private static JLabel keysLabel;
	
	private static GridBagLayout gridbag;
	private static GridBagLayout kvpGridBag;
	
	private static JButton mCancel;
	private static JButton mReplace;
	private static JButton mPlus;
	private static JButton mMinus;
	
	private static JPanel kvpPanel;
	private static JPanel textFieldsAndKVP;
	private static JPanel textControlsPane;
	
	private static JSplitPane fieldAndButton;
	
	private static Font normalFont;
	
	private  Font italicFont;
	
	private static void addKeyValuePairRowsComps(ArrayList<JTextField> keys,
            ArrayList<JTextField> values, GridBagLayout gridbag,
            Container container) {
		GridBagConstraints c = new GridBagConstraints();
		c.anchor = GridBagConstraints.EAST;
		int numLabels = keys.size();
		for (int i = 0; i < numLabels; i++) {
			c.gridwidth = GridBagConstraints.EAST; //next-to-last
			c.fill = GridBagConstraints.NONE;      //reset to default
			c.weightx = 0.0;                       //reset to default
			container.add(keys.get(i), c);
			c.fill = GridBagConstraints.NONE;      //reset to default
			c.gridwidth = GridBagConstraints.CENTER; //next-to-last
			container.add(Box.createHorizontalStrut(50), c);
			JLabel newEqual = new JLabel("=");
			container.add(newEqual, c);
			container.add(Box.createHorizontalStrut(50), c);
			c.fill = GridBagConstraints.HORIZONTAL;      //reset to default
			c.gridwidth = GridBagConstraints.REMAINDER;     //end row
			c.weightx = 1.0;
			container.add(values.get(i), c);
		}
	}
	
	private static void addLabelTextRowsComps(ArrayList<JLabel> labels2,
            ArrayList<Component> comps, GridBagLayout gridbag,
            Container container) {
		GridBagConstraints c = new GridBagConstraints();
		c.anchor = GridBagConstraints.EAST;
		int numLabels = labels2.size();
		for (int i = 0; i < numLabels; i++) {
			c.gridwidth = GridBagConstraints.RELATIVE; //next-to-last
			c.fill = GridBagConstraints.NONE;      //reset to default
			c.weightx = 0.0;                       //reset to default
			container.add(labels2.get(i), c);
			c.gridwidth = GridBagConstraints.REMAINDER;     //end row
			c.fill = GridBagConstraints.HORIZONTAL;
			c.weightx = 1.0;
			container.add(comps.get(i), c);
		}
	}
	
	static void paneRemover(JPanel panel, Component... comp){
		for(Component c: comp){
			panel.remove(c);
		}
	}
	
	static void paneAdder(JPanel panel, Component... comp){
		for(Component c: comp){
			panel.add(c);
		}
	}
	
	static void repainter(JPanel panel){
		panel.invalidate();
		panel.repaint();
		panel.validate();
	}
	
	class CancelListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			
		}
		
	}
	
	class ReplaceListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			
		}
		
	}
	
	class InverseMouseListener implements MouseListener{

		@Override
		public void mouseClicked(MouseEvent e) {
			// TODO Auto-generated method stub	
		}

		@Override
		public void mousePressed(MouseEvent e) {
			// TODO Auto-generated method stub	
		}

		@Override
		public void mouseReleased(MouseEvent e) {
			// TODO Auto-generated method stub	
		}

		@Override
		public void mouseEntered(MouseEvent e) {
			// TODO Auto-generated method stub	
		}

		@Override
		public void mouseExited(MouseEvent e) {
			// TODO Auto-generated method stub	
		}		
	}
	
	class kvpHinter implements MouseListener{
		boolean firstClick = true;

		@Override
		public void mouseClicked(MouseEvent e) {
			// TODO Auto-generated method stub
			if (firstClick){
				JTextField eT = (JTextField) e.getComponent();
				eT.setText("");
				firstClick = false;
			}
		}

		@Override
		public void mousePressed(MouseEvent e) {
			// TODO Auto-generated method stub	
		}

		@Override
		public void mouseReleased(MouseEvent e) {
			// TODO Auto-generated method stub	
		}

		@Override
		public void mouseEntered(MouseEvent e) {
			// TODO Auto-generated method stub	
		}

		@Override
		public void mouseExited(MouseEvent e) {
			// TODO Auto-generated method stub	
		}	
	}
	
	class MinusListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub0
			if(keysList.size() > 1){
				paneRemover(textFieldsAndKVP, kvpPanel);
			    kvpPanel = new JPanel();
			    kvpPanel.setLayout(kvpGridBag);
				keysList.remove(keysList.size()-1);
				valuesList.remove(keysList.size()-1);
			    addKeyValuePairRowsComps(keysList, valuesList, kvpGridBag, kvpPanel);
				textFieldsAndKVP.add(kvpPanel);
				repainter(kvpPanel);
				repainter(textFieldsAndKVP);
				repainter(editPane);
			}
		}		
	}
	
	class PlusListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			paneRemover(textFieldsAndKVP, kvpPanel);
			paneRemover(editPane, textFieldsAndKVP);
		    kvpPanel = new JPanel();
		    kvpPanel.setLayout(kvpGridBag);
			JTextField tempKeys = new JTextField(10);
			tempKeys.setText("Key");
			tempKeys.setForeground(Color.gray);
			tempKeys.setFont(italicFont);
			tempKeys.addMouseListener(new kvpHinter());
			JTextField tempValues = new JTextField(10);
			tempValues.setText("Value");
			tempValues.setForeground(Color.gray);
			tempValues.setFont(italicFont);
			tempValues.addMouseListener(new kvpHinter());

			keysList.add(tempKeys);
			valuesList.add(tempValues);
		    addKeyValuePairRowsComps(keysList, valuesList, kvpGridBag, kvpPanel);
			textFieldsAndKVP.add(kvpPanel);
			repainter(kvpPanel);
			repainter(textFieldsAndKVP);
		    editPane.add(textFieldsAndKVP);
			repainter(editPane);
		}	
 	}
	
	public JPanel editPanel(){
		
		normalFont = new Font("Arial", Font.PLAIN, 14);
	    italicFont = new Font("Arial", Font.ITALIC, 14);
		
		String [] restCalls = { "POST" , "GET" };
		restCallType = new JComboBox<Object>(restCalls);
		restCallType.setActionCommand(restCallString);
		 
		urlTextField = new JTextField(10);
	    urlTextField.setActionCommand(urlString);
	    
	    compsComp = new ArrayList<Component>();
	    compsComp.add(restCallType);
	    compsComp.add(urlTextField);

	    valuesToSend = new JTextField(10);
	    valuesToSend.setActionCommand(valueString);
	    valuesToSend.setText(valueString);
	    valuesToSend.setForeground(Color.gray);
	    valuesToSend.setFont(italicFont);
	    valuesToSend.addMouseListener(new kvpHinter());
	    
	    valuesLabel = new JLabel();
	    valuesLabel.setLabelFor(valuesToSend);
	    
	    valuesList = new ArrayList<JTextField>();
	    valuesList.add(valuesToSend);
	    
	    keysToSend = new JTextField(10);
	    keysToSend.setActionCommand(keyString);
	    keysToSend.setText(keyString);
	    keysToSend.setForeground(Color.gray);
	    keysToSend.setFont(italicFont);
	    keysToSend.addMouseListener(new kvpHinter());
	    
	    keysLabel = new JLabel(keyString + ": ");
	    keysLabel.setLabelFor(keysToSend);
	    
	    keysList = new ArrayList<JTextField>();
	    keysList.add(keysToSend);
	     
	    restCallLabel = new JLabel(restCallString + ": ");
	    restCallLabel.setFont(normalFont);
	    restCallLabel.setLabelFor(restCallType);
	     
	    urlLabel = new JLabel(urlString + ": ");
	    urlLabel.setLabelFor(urlTextField);
	    
	    labels.add(restCallLabel);
	    labels.add(urlLabel);
	    for(JLabel label : labels){
	    	label.setFont(QuantumStyleManager.mightyFont());
	    }
	     
	    textFields.add(urlTextField);
	     
	    kvpPanel = new JPanel();
	    kvpGridBag = new GridBagLayout();
	    GridBagConstraints kvpC = new GridBagConstraints();
	    kvpPanel.setLayout(kvpGridBag);
	    kvpC.gridwidth = GridBagConstraints.REMAINDER; //last
	    kvpC.anchor = GridBagConstraints.WEST;
	    kvpC.weightx = 1.0;
	    
	    mPlus = new JButton("+");
	    mPlus.addActionListener(new PlusListener());
	    mMinus = new JButton("-");
	    mMinus.addActionListener(new MinusListener());
	    QuantumStyleManager.buttonStyles(mPlus, mMinus);
	    
	    JPanel plusMinusPanel = new JPanel();
	    plusMinusPanel.add(mPlus);
	    plusMinusPanel.add(Box.createHorizontalStrut(320));
	    plusMinusPanel.add(mMinus);
	    
	    for (JComboBox<?> comboBox: comboBoxes){
	    	comboBox.setUI(QuantumStyleManager.ColorArrowUI.createUI(restCallType));
	    }
	    
	    textControlsPane = new JPanel();
	    gridbag = new GridBagLayout();
	    GridBagConstraints c = new GridBagConstraints();
	    textControlsPane.setLayout(gridbag);
	    addLabelTextRowsComps(labels, compsComp, gridbag, textControlsPane);
	    c.gridwidth = GridBagConstraints.REMAINDER; //last
	    c.anchor = GridBagConstraints.WEST;
	    c.weightx = 1.0;
	    
	    mReplace = new JButton(replaceString);
	    mReplace.addActionListener(new ReplaceListener());
	    JPanel miniPane = new JPanel(new BorderLayout());
	    QuantumStyleManager.buttonStyles(mReplace);
	    miniPane.add(Box.createHorizontalGlue());
	    miniPane.add(mReplace);
	    
	    textFieldsAndKVP = new JPanel(new BorderLayout());
	    textFieldsAndKVP.add(textControlsPane, BorderLayout.NORTH);
	    textFieldsAndKVP.add(kvpPanel, BorderLayout.CENTER);
	    textFieldsAndKVP.add(plusMinusPanel, BorderLayout.SOUTH);
	    textFieldsAndKVP.setBorder(
	            BorderFactory.createCompoundBorder(
	                            BorderFactory.createTitledBorder(getBorder(), "Edit Your Tag!",
	                            		TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
	                            BorderFactory.createEmptyBorder(5,5,5,5)));
	    fieldAndButton = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
	    	 textFieldsAndKVP,
	    			miniPane);
	    
	    editPane = new JPanel(new BorderLayout());
	    editPane.add(fieldAndButton);
		
		return editPane;
	}
	
}