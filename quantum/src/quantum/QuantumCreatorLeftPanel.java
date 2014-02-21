package quantum;

import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.LinkedHashMap;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.JTextField;
import javax.swing.border.TitledBorder;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class QuantumCreatorLeftPanel extends JPanel{
	/**
	 * 
	 */
	private static final long serialVersionUID = 3708802608955076447L;
	protected static final String textFieldString = "Tag Name";
    protected static final String passwordFieldString = "Identifier Type";
    protected static final String ftfString = "Identifier";
    protected static final String actionString = "Action";
    protected static final String sendKeysString = "URL: ";
    protected static final String buttonString = "JButton";
	protected static JPanel leftPane;
	
	class ComboListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			if(actionType.getSelectedItem().toString().equals("Go To")){
				compsComp.clear();
				labels.clear();
				
				genericAdder(compsComp, actionType, keysToSend);
				genericAdder(labels, actionFieldLabel, sendKeysFieldLabel);
				
			    addLabelTextRowsComps(labels, compsComp, gridbag, textControlsPane);
				paneRemover(textControlsPane, tagName, identifierType, identifierTextField, textFieldLabel, passwordFieldLabel,identifierLabel);
				sendKeysFieldLabel.setText("URL: ");
				Component[] comps = textControlsPane.getComponents();
				boolean compCheck = false;
				for(Component comp: comps){
					if(comp == keysToSend){
						compCheck = true;
					}
				}
				if(compCheck == false){
					textControlsPane.add(keysToSend);
				}
				
				repainter(leftPane);
			}
			else if(actionType.getSelectedItem().toString().equals("Enter Text") || actionType.getSelectedItem().toString().equals("Enter Text and Submit")){
				compsComp.clear();
				labels.clear();
				
				genericAdder(compsComp, actionType, keysToSend, tagName, identifierType, identifierTextField);
				genericAdder(labels, actionFieldLabel, sendKeysFieldLabel, textFieldLabel, passwordFieldLabel,identifierLabel);
				
			    textControlsPane.removeAll();
				sendKeysFieldLabel.setText("Text: ");
				paneAdder(textControlsPane,
						actionType,
						keysToSend,
						tagName,
						identifierType,
						identifierTextField, 
						actionFieldLabel,
						sendKeysFieldLabel,
						textFieldLabel,
						passwordFieldLabel,
						identifierLabel
						);	
			    addLabelTextRowsComps(labels, compsComp, gridbag, textControlsPane);
				repainter(leftPane);

			}
			else{
				compsComp.clear();
				labels.clear();
				
				genericAdder(compsComp, actionType, tagName, identifierType, identifierTextField);
				genericAdder(labels, actionFieldLabel, textFieldLabel, passwordFieldLabel,identifierLabel);
				
			    addLabelTextRowsComps(labels, compsComp, gridbag, textControlsPane);
			    
				paneAdder(textControlsPane, tagName, identifierType, identifierTextField, textFieldLabel, passwordFieldLabel, identifierLabel);
				paneRemover(textControlsPane, keysToSend, sendKeysFieldLabel);

			    addLabelTextRowsComps(labels, compsComp, gridbag, textControlsPane);
				
				repainter(leftPane);

			}
		}
 		
 	}
	
	class SubmitListener implements ActionListener{
		LinkedHashMap<String, String> subContainer = new LinkedHashMap<String, String>();
		@Override
		public void actionPerformed(ActionEvent e) {
			int n = QuantumDataManager.creatorMap.size();
			// TODO Auto-generated method stub
			if(actionType.getSelectedItem().toString().equals("Go To")){
				subContainer.put("URL", keysToSend.getText());
				if(n == 0){
					QuantumDataManager.baseClassURL = keysToSend.getText();
				}
				QuantumDataManager.creatorMap.put(n, subContainer);
				
				QuantumCreatorList.listConstructor(n);
				
				subContainer = new LinkedHashMap<String, String>();
			}
			else if(actionType.getSelectedItem().toString().equals("Enter Text")){
				ArrayList<String> tempContainer = new ArrayList<String>();
				tempContainer.add(keysToSend.getText());
				tempContainer.add(tagName.getSelectedItem().toString());
				tempContainer.add(identifierType.getSelectedItem().toString());
				tempContainer.add(identifierTextField.getText());
				String[] tempArray = new String[tempContainer.size()];
				
				tempArray = tempContainer.toArray(tempArray);
				StringBuilder sb = new StringBuilder(64);
				for(String tempstr : tempArray){
					sb.append(tempstr + ",");
				}
				subContainer.put("TEXT", sb.toString());
				QuantumDataManager.creatorMap.put(n, subContainer);
				
				QuantumCreatorList.listConstructor(n);
				
				subContainer = new LinkedHashMap<String, String>();
			}
			else if(actionType.getSelectedItem().toString().equals("Enter Text and Submit")){
				ArrayList<String> tempContainer = new ArrayList<String>();
				tempContainer.add(keysToSend.getText());
				tempContainer.add(tagName.getSelectedItem().toString());
				tempContainer.add(identifierType.getSelectedItem().toString());
				tempContainer.add(identifierTextField.getText());
				String[] tempArray = new String[tempContainer.size()];
				
				tempArray = tempContainer.toArray(tempArray);
				StringBuilder sb = new StringBuilder(64);
				for(String tempstr : tempArray){
					sb.append(tempstr + ",");
				}
				subContainer.put("SUBMIT", sb.toString());
				QuantumDataManager.creatorMap.put(n, subContainer);
				
				QuantumCreatorList.listConstructor(n);
				
				subContainer = new LinkedHashMap<String, String>();
			}
			else{
				ArrayList<String> tempContainer = new ArrayList<String>();
				tempContainer.add(tagName.getSelectedItem().toString());
				tempContainer.add(identifierType.getSelectedItem().toString());
				tempContainer.add(identifierTextField.getText());
				String[] tempArray = new String[tempContainer.size()];
				
				tempArray = tempContainer.toArray(tempArray);
				StringBuilder sb = new StringBuilder(64);
				for(String tempstr : tempArray){
					sb.append(tempstr + ",");
				}
				subContainer.put("CLICK", sb.toString());
				QuantumDataManager.creatorMap.put(n, subContainer);
				
				QuantumCreatorList.listConstructor(n);
				
				subContainer = new LinkedHashMap<String, String>();
			}
			n++;
		}

	}
	
	/*
	 * top controller panel
	 */
	private JPanel textControlsPane;
	/*
	 * combo boxes
	 */
	private JComboBox<Object> actionType;
	private JComboBox<Object> tagName;
	private JComboBox<Object> identifierType;
	private JTextField identifierTextField;
	private JTextField keysToSend;
	private ArrayList<JComboBox<?>> comboBoxes = new ArrayList<JComboBox<?>>();
	private ArrayList<JTextField> textFields = new ArrayList<JTextField>();
	private ArrayList<JLabel> labels = new ArrayList<JLabel>();
	private JLabel textFieldLabel;
	private JLabel passwordFieldLabel;
	private JLabel identifierLabel;
	private JLabel actionFieldLabel;
	private JLabel sendKeysFieldLabel;
	private GridBagLayout gridbag;
	private ArrayList<Component> compsComp;
	private JButton mSubmit;
	
	
	public JPanel leftPanel(){
	     //Create a regular text field.
	 	 String [] actions = { "Go To" , "Click", "Enter Text", "Enter Text and Submit" };
	  	 actionType = new JComboBox<Object>(actions);
	     actionType.setActionCommand(actionString);
	     actionType.addActionListener(new ComboListener());
		     
	     tagName = new JComboBox<Object>(QuantumTagList.tagList());
	     tagName.setActionCommand(textFieldString);
	     
	     //Create a password field.
	     String [] identifierTypes = {"Class Name", "ID", "Link Text", "CSS Selector", "Name", "Partial Link Text", "XPath"};
	     identifierType = new JComboBox<Object>(identifierTypes);
	     identifierType.setActionCommand(passwordFieldString);
	
	     //Create a formatted text field.
	     identifierTextField = new JTextField(10);
	     identifierTextField.setActionCommand(ftfString);
	     
	     
	     keysToSend = new JTextField(10);
	     keysToSend.setActionCommand(sendKeysString);
	
	     textFieldLabel = new JLabel(textFieldString + ": ");
	     textFieldLabel.setLabelFor(tagName);
	     passwordFieldLabel = new JLabel(passwordFieldString + ": ");
	     passwordFieldLabel.setLabelFor(identifierType);
	     identifierLabel = new JLabel(ftfString + ": ");
	     identifierLabel.setLabelFor(identifierTextField);
	     actionFieldLabel = new JLabel(actionString + ": ");
	     actionFieldLabel.setLabelFor(actionType);
	     sendKeysFieldLabel = new JLabel(sendKeysString + ": ");
	     sendKeysFieldLabel.setLabelFor(keysToSend);
	     //Create a label to put messages during an action event.
	
	     //Lay out the text controls and the labels.
	     textControlsPane = new JPanel();
	     gridbag = new GridBagLayout();
	     GridBagConstraints c = new GridBagConstraints();
	
	     textControlsPane.setLayout(gridbag);
	     
	     labels.add(actionFieldLabel);
	     labels.add(sendKeysFieldLabel);
	     for(JLabel label : labels){
	     	label.setFont(QuantumStyleManager.mightyFont());
	     }
	     textFields.add(identifierTextField);
	     textFields.add(keysToSend);
	     comboBoxes.add(actionType);
	     comboBoxes.add(tagName);
	     comboBoxes.add(identifierType);
	     for (JComboBox<?> comboBox: comboBoxes){
	     	comboBox.setUI(QuantumStyleManager.ColorArrowUI.createUI(actionType));
	     }
	     compsComp = new ArrayList<Component>();
	     compsComp.add(actionType);
	     compsComp.add(keysToSend);
	     //addLabelTextRows(labels, textFields, comboBoxes, gridbag, textControlsPane);
	     addLabelTextRowsComps(labels, compsComp, gridbag, textControlsPane);
	     c.gridwidth = GridBagConstraints.REMAINDER; //last
	     c.anchor = GridBagConstraints.WEST;
	     c.weightx = 1.0;
	     textControlsPane.setBorder(
	             BorderFactory.createCompoundBorder(
	                             BorderFactory.createTitledBorder(getBorder(), "Searchers",
	                             		TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
	                             BorderFactory.createEmptyBorder(5,5,5,5)));
	     paneRemover(textControlsPane, tagName, identifierType, identifierTextField, textFieldLabel, passwordFieldLabel,identifierLabel);
	     leftPane = new JPanel(new BorderLayout());
	     
	     mSubmit = new JButton("Create Step");
	     mSubmit.addActionListener(new SubmitListener());
	     JPanel miniPane = new JPanel(new BorderLayout());
	     QuantumStyleManager.buttonStyles(mSubmit);
	     miniPane.add(mSubmit);
	     JSplitPane fieldAndButton = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
	    		 	textControlsPane,
	     			miniPane);
	     
	     QuantumCreatorList qList = new QuantumCreatorList();
	     final JSplitPane quantumDataList = qList.QuantumList();
	     //HireListener hireListener = new HireListener(mSubmit);
	     
	     QuantumCreatorList.list.addListSelectionListener(new ListSelectionListener() {
				@Override
				public void valueChanged(ListSelectionEvent e) {
					// TODO Auto-generated method stub
					//QuantumList.list.setSelectedIndex(QuantumList.listModel.size()-1);
					QuantumCreatorList.fireButton.setEnabled(true);
					QuantumCreatorList.moveUpButton.setEnabled(true);
					QuantumCreatorList.runAllButton.setEnabled(true);
				}  	
	     });
	     
	     mSubmit.setMaximumSize(new Dimension(30,30));
	     mSubmit.setPreferredSize(new Dimension(30,30));
	     JSplitPane all = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
	    		 fieldAndButton,
	    		 quantumDataList);
	     leftPane.add(all, 
	                  BorderLayout.PAGE_START);
	     /*leftPane.add(quantumDataList,
	     		BorderLayout.PAGE_END);*/
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
	static void genericRemover(@SuppressWarnings("rawtypes") ArrayList a, Object... b){
		for (Object c: b){
			a.remove(c);
		}
	}
	@SuppressWarnings("unchecked")
	static void genericAdder(@SuppressWarnings("rawtypes") ArrayList a, Object... b){
		for (Object c: b){
			a.add(c);
		}
	}
}
