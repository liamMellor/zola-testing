package quantum;

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
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.JTextField;
import javax.swing.border.TitledBorder;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class APIshCreatorLeftPanel extends JPanel{
	/**
	 * 
	 */
	private static final long serialVersionUID = 3708802608955076447L;
	protected static final String urlString = "Base URL";
    protected static final String restCallString = "REST call";
    protected static final String keyString = "Key";
    protected static final String valueString = "Value";
    protected static final String buttonString = "JButton";
	protected static JPanel leftPane;
	
	
	class SubmitListener implements ActionListener{
		int n;
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			APIshDataManager.requestType.add(restCallType.getSelectedItem().toString());
			APIshDataManager.urlUp.add(urlTextField.getText());
			LinkedHashMap<String, String> tempMapper = new LinkedHashMap<String, String>();
			for(int j = 0; j < keysList.size(); j++){
				tempMapper.put(keysList.get(j).getText(), valuesList.get(j).getText());
			}
			APIshDataManager.creationContainer.put(n, tempMapper);
			APIshCreatorList.listConstructor(n);
			n++;
		}

	}
	class MinusListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub0
			if(keysList.size() > 1){
				textFieldsAndKVP.remove(kvpPanel);
				keysList.remove(keysList.size()-1);
				valuesList.remove(valuesList.size()-1);
				System.out.println(keysList.size());
				textFieldsAndKVP.add(kvpPanel);
				repainter(kvpPanel);
				repainter(textFieldsAndKVP);
				repainter(leftPane);
			}
			
			else{
				System.out.println("ERROR: Already reached minimum amount of key value pairs.");
			}
			
		}
		
		
	}
	class PlusListener implements ActionListener{


		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			paneRemover(textFieldsAndKVP, kvpPanel);
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
			repainter(leftPane);
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
	/*
	 * top controller panel
	 */
	private JPanel textControlsPane;
	/*
	 * combo boxes
	 */
	private JComboBox<Object> restCallType;
	private JTextField urlTextField;
	private JTextField keysToSend;
	private JTextField valuesToSend;
	private ArrayList<JComboBox> comboBoxes = new ArrayList<JComboBox>();
	private ArrayList<JTextField> textFields = new ArrayList<JTextField>();
	private ArrayList<JLabel> labels = new ArrayList<JLabel>();
	private JLabel restCallLabel;
	private JLabel urlLabel;
	private JLabel valuesLabel;
	private JLabel keysLabel;
	private GridBagLayout gridbag;
	private ArrayList<Component> compsComp;
	private JButton mSubmit;
	private JButton mPlus;
	private JButton mMinus;
	private Font normalFont;
	private Font italicFont;
	private JPanel kvpPanel;
	private GridBagLayout kvpGridBag;
	private ArrayList<JTextField> keysList;
	private ArrayList<JTextField> valuesList;
	private JPanel textFieldsAndKVP;
	
	
	public JPanel leftPanel(){
	     //Create a regular text field.
	 	 String [] restCalls = { "POST" , "GET" };
	 	restCallType = new JComboBox<Object>(restCalls);
	 	restCallType.setActionCommand(restCallString);
	 	//restCallType.addActionListener(new ComboListener());
	
	     //Create a formatted text field.
	     urlTextField = new JTextField(10);
	     urlTextField.setActionCommand(urlString);
	     
	     valuesToSend = new JTextField(10);
	     valuesToSend.setActionCommand(valueString);
	     
	     keysToSend = new JTextField(10);
	     keysToSend.setActionCommand(keyString);
	     
	     normalFont = new Font("Arial", Font.PLAIN, 14);
	
	     restCallLabel = new JLabel(restCallString + ": ");
	     restCallLabel.setFont(normalFont);
	     restCallLabel.setLabelFor(restCallType);
	     urlLabel = new JLabel(urlString + ": ");
	     urlLabel.setLabelFor(urlTextField);
	     valuesLabel = new JLabel();
	     valuesLabel.setLabelFor(valuesToSend);
	     keysLabel = new JLabel(keyString + ": ");
	     keysLabel.setLabelFor(keysToSend);
	     //Create a label to put messages during an action event.
	
	     //Lay out the text controls and the labels.
	     textControlsPane = new JPanel();
	     gridbag = new GridBagLayout();
	     GridBagConstraints c = new GridBagConstraints();
	
	     textControlsPane.setLayout(gridbag);
	     
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
	     
	     italicFont = new Font("Arial", Font.ITALIC, 14);
	     
	     keysToSend.setText("Key");
	     keysToSend.setForeground(Color.gray);
	     keysToSend.setFont(italicFont);
	     
	     keysToSend.addMouseListener(new kvpHinter());
	     	     
	     valuesToSend.setText("Value");
	     valuesToSend.setForeground(Color.gray);
	     valuesToSend.setFont(italicFont);
	     
	     valuesToSend.addMouseListener(new kvpHinter());
	     keysList = new ArrayList<JTextField>();
	     valuesList = new ArrayList<JTextField>();
	     
	     keysList.add(keysToSend);
	     valuesList.add(valuesToSend);
	     addKeyValuePairRowsComps(keysList, valuesList, kvpGridBag, kvpPanel);
	     textFields.add(keysToSend);
	     textFields.add(valuesToSend);
	     comboBoxes.add(restCallType);
	     
	     JPanel plusMinusPanel = new JPanel();
	     
	     mPlus = new JButton("+");
	     mPlus.addActionListener(new PlusListener());
	     mMinus = new JButton("-");
	     mMinus.addActionListener(new MinusListener());
	     
	     QuantumStyleManager.buttonStyles(mPlus, mMinus);
	     
	     plusMinusPanel.add(mPlus);
	     plusMinusPanel.add(Box.createHorizontalStrut(320));
	     plusMinusPanel.add(mMinus);
	     
	     for (JComboBox<?> comboBox: comboBoxes){
	     	comboBox.setUI(QuantumStyleManager.ColorArrowUI.createUI(restCallType));
	     }
	     compsComp = new ArrayList<Component>();
	     compsComp.add(restCallType);
	     compsComp.add(urlTextField);
	     addLabelTextRowsComps(labels, compsComp, gridbag, textControlsPane);
	     c.gridwidth = GridBagConstraints.REMAINDER; //last
	     c.anchor = GridBagConstraints.WEST;
	     c.weightx = 1.0;
	     
	     leftPane = new JPanel(new BorderLayout());
	     
	     
	     mSubmit = new JButton("Submit Step");
	     mSubmit.addActionListener(new SubmitListener());
	     JPanel miniPane = new JPanel(new BorderLayout());
	     QuantumStyleManager.buttonStyles(mSubmit);
	     miniPane.add(Box.createHorizontalGlue());
	     miniPane.add(mSubmit);
	     
	     textFieldsAndKVP = new JPanel(new BorderLayout());
	     textFieldsAndKVP.add(textControlsPane, BorderLayout.NORTH);
	     textFieldsAndKVP.add(kvpPanel, BorderLayout.CENTER);
	     textFieldsAndKVP.add(plusMinusPanel, BorderLayout.SOUTH);
	     textFieldsAndKVP.setBorder(
	             BorderFactory.createCompoundBorder(
	                             BorderFactory.createTitledBorder(getBorder(), "Build Your Tag!",
	                             		TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
	                             BorderFactory.createEmptyBorder(5,5,5,5)));
	     JSplitPane fieldAndButton = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
	    		 textFieldsAndKVP,
	     			miniPane);
	     
	     APIshCreatorList aList = new APIshCreatorList();
	     final JSplitPane apishDataList = aList.APIshList();
	     //HireListener hireListener = new HireListener(mSubmit);
	     
	     APIshCreatorList.list.addListSelectionListener(new ListSelectionListener() {
				@Override
				public void valueChanged(ListSelectionEvent e) {
					// TODO Auto-generated method stub
					APIshCreatorList.editButton.setEnabled(true);
					APIshCreatorList.deleteButton.setEnabled(true);
					APIshCreatorList.runButton.setEnabled(true);
				}  	
	     });
	     
	     mSubmit.setMaximumSize(new Dimension(30,30));
	     mSubmit.setPreferredSize(new Dimension(30,30));
	     leftPane.add(fieldAndButton, 
	                  BorderLayout.PAGE_START);
	     leftPane.add(apishDataList,
	     		BorderLayout.PAGE_END);
	 	return leftPane;
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
	static void genericRemover(ArrayList a, Object... b){
		for (Object c: b){
			a.remove(c);
		}
	}
	static void genericAdder(ArrayList a, Object... b){
		for (Object c: b){
			a.add(c);
		}
	}
}
