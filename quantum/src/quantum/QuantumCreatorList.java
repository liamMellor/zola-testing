package src.quantum;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map.Entry;

import javax.swing.BorderFactory;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSeparator;
import javax.swing.JSplitPane;
import javax.swing.ListSelectionModel;
import javax.swing.SwingConstants;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class QuantumCreatorList {
	
	static JList<String> list;
    static DefaultListModel<String> listModel;

    private static final String moveUpString = "Edit";
    private static final String runAllString = "Run All";
    private static final String fireString = "Remove";
    static JButton fireButton;
    static JButton moveUpButton;
    static JButton runAllButton;
    
    public JSplitPane QuantumList() {

        listModel = new DefaultListModel<String>();
        listModel.addElement("");

        //Create the list and put it in a scroll pane.
        list = new JList<String>(listModel);
        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        list.setSelectedIndex(0);
        list.addListSelectionListener(new ListSelectionListener(){

			@Override
			public void valueChanged(ListSelectionEvent e) {
				// TODO Auto-generated method stub
			}
        	
        });
        list.setVisibleRowCount(5);
        JScrollPane listScrollPane = new JScrollPane(list);

        //HireListener hireListener = new HireListener(hireButton);
        //hireButton.setActionCommand(hireString);
        //hireButton.addActionListener(hireListener);

        fireButton = new JButton(fireString);
        fireButton.setActionCommand(fireString);
        fireButton.addActionListener(new FireListener());
        
        moveUpButton = new JButton(moveUpString);
        moveUpButton.setActionCommand(moveUpString);
        moveUpButton.addActionListener(new EditorListener());
        
        runAllButton = new JButton(runAllString);
        runAllButton.setActionCommand(runAllString);
        runAllButton.addActionListener(new RunAllListener());
        
        QuantumStyleManager.buttonStyles(fireButton,moveUpButton,runAllButton);

        //Create a panel that uses BoxLayout.
        JPanel buttonPane = new JPanel();
        buttonPane.setLayout(new BoxLayout(buttonPane,
                                           BoxLayout.LINE_AXIS));
        buttonPane.add(fireButton);
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(new JSeparator(SwingConstants.VERTICAL));
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(moveUpButton);
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(new JSeparator(SwingConstants.VERTICAL));
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(runAllButton);
        buttonPane.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
        listScrollPane.setPreferredSize(new Dimension(400, 560));
        buttonPane.setPreferredSize(new Dimension(20, 20));
        JSplitPane listWithButtons = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        listScrollPane,
        buttonPane);
        listModel.removeAllElements();
        fireButton.setEnabled(false);
        moveUpButton.setEnabled(false);
        runAllButton.setEnabled(false);
		return listWithButtons;

    }
    public static void listConstructor(int n){
    	StringBuilder sb = new StringBuilder(64);
    	sb.append("<html>");
    	sb.append("<b><i>Step " + (n+1) + ". </i></b><br>");
    	LinkedHashMap<String, String> listMap = QuantumDataManager.creatorMap.get(n);
    	for( Entry<String, String> listEntry : listMap.entrySet()){
        	sb.append("<b>Action: </b>" + listEntry.getKey());
        	if(listEntry.getKey().equals("URL")){
        		sb.append("<br><b>URL: </b>" + listEntry.getValue());
        		sb.append("</html>");
        		listModel.addElement(sb.toString());
        	}
        	else if (listEntry.getKey().equals("TEXT") || listEntry.getKey().equals("SUBMIT")){
        		String valueFull = listEntry.getValue();
        		String[] valueSplit = valueFull.split(",");
        		sb.append("		<b>Tag Type: </b>" + valueSplit[1] + "<br>");
        		sb.append("<b>Identifier: </b>" + valueSplit[3]);
        		sb.append("		<b>Id Type: </b>" + valueSplit[2] + "<br>");
        		sb.append("<b>Text Submitted: </b>" + valueSplit[0]);
        		sb.append("</html>");
        		listModel.addElement(sb.toString());
        	}
        	else if (listEntry.getKey().equals("CLICK")){
        		String valueFull = listEntry.getValue();
        		String[] valueSplit = valueFull.split(",");
        		sb.append("		<b>Tag Type: </b>" + valueSplit[0] + "<br>");
        		sb.append("<b>Identifier: </b>" + valueSplit[2]);
        		sb.append("		<b>Id Type: </b>" + valueSplit[1] + "<br>");
        		sb.append("</html>");
        		listModel.addElement(sb.toString());
        	}
    	}
    }
    public static void listValueChanged(ListSelectionEvent e) {
        if (e.getValueIsAdjusting() == false) {

            if (list.getSelectedIndex() == -1) {
            //No selection, disable fire button.
                fireButton.setEnabled(false);

            } else {
            //Selection, enable the fire button.
                fireButton.setEnabled(true);
            }
        }
    }
    class FireListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            //This method can be called only if
            //there's a valid selection
            //so go ahead and remove whatever's selected.
            int index = list.getSelectedIndex();
            listModel.remove(index);
            QuantumDataManager.creatorMap.remove(index);
            int size = listModel.getSize();

            if (size == 0) { //Nobody's left, disable firing.
                fireButton.setEnabled(false);

            } else { //Select an index.
                if (index == listModel.getSize()) {
                    //removed item in last position
                    index--;
                }

                list.setSelectedIndex(index);
                list.ensureIndexIsVisible(index);
            }
        }
    }
    class EditorListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			
		}
    }
    class RunAllListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
					// TODO Auto-generated method stub
					//QuantumDataManager.baseClassURL = baseUrl.getText().toString();
					QuantumRunner.run();
					QuantumCreatorMain.terminal.append(QuantumDataManager.runnerConsole);
		}
    }
}
