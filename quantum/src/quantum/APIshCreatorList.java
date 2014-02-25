package quantum;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map.Entry;
import java.util.Set;
import java.util.TreeMap;

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

public class APIshCreatorList {
	
	static JList list;
    static DefaultListModel listModel;

    private static final String editString = "Edit Step";
    private static final String deleteString = "Delete Step";
    private static final String runString = "Run Test";
    static JButton editButton;
    static JButton deleteButton;
    static JButton runButton;
    
    public JSplitPane APIshList() {

        listModel = new DefaultListModel();
        listModel.addElement("");

        //Create the list and put it in a scroll pane.
        list = new JList(listModel);
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

        editButton = new JButton(editString);
        editButton.setActionCommand(editString);
        editButton.addActionListener(new EditorListener());
        
        deleteButton = new JButton(deleteString);
        deleteButton.setActionCommand(deleteString);
        deleteButton.addActionListener(new FireListener());
        
        runButton = new JButton(runString);
        runButton.setActionCommand(runString);
        runButton.addActionListener(new RunListener());
        
        QuantumStyleManager.buttonStyles(editButton,deleteButton,runButton);

        //employeeName.addActionListener(hireListener);
        //employeeName.getDocument().addDocumentListener(hireListener);
        String name = listModel.getElementAt(
                              list.getSelectedIndex()).toString();

        //Create a panel that uses BoxLayout.
        JPanel buttonPane = new JPanel();
        buttonPane.setLayout(new BoxLayout(buttonPane,
                                           BoxLayout.LINE_AXIS));
        buttonPane.add(editButton);
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(new JSeparator(SwingConstants.VERTICAL));
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(deleteButton);
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(new JSeparator(SwingConstants.VERTICAL));
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(runButton);
        buttonPane.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
        listScrollPane.setPreferredSize(new Dimension(400, 560));
        buttonPane.setPreferredSize(new Dimension(20, 20));
        JSplitPane listWithButtons = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        listScrollPane,
        buttonPane);
        listModel.removeAllElements();
        editButton.setEnabled(false);
        deleteButton.setEnabled(false);
        runButton.setEnabled(false);
		return listWithButtons;

        //add(listScrollPane, BorderLayout.CENTER);
        //add(buttonPane, BorderLayout.PAGE_END);
    }
    
    public static void listConstructor(int n){
    	StringBuilder sb = new StringBuilder(64);
    	sb.append("<html>");
    	sb.append("Step " + (n+1) + ".<br>");
    	LinkedHashMap<String, String> listMap = APIshDataManager.creationContainer.get(n);
    	String currentUrl = APIshDataManager.urlUp.get(n);
    	String restType = APIshDataManager.requestType.get(n);
    	sb.append("<br><b>URL: </b>" + currentUrl);
		sb.append("<br><b>Call: </b>" + restType);
    	for( Entry<String, String> listEntry : listMap.entrySet()){
    		sb.append("<br><b> Key-Value: </b>" + listEntry.getKey() + " = " + listEntry.getValue());
    	}
		sb.append("</html>");
		listModel.addElement(sb.toString());
    }
    public static void listValueChanged(ListSelectionEvent e) {
        if (e.getValueIsAdjusting() == false) {

            if (list.getSelectedIndex() == -1) {
            //No selection, disable fire button.
                editButton.setEnabled(false);

            } else {
            //Selection, enable the fire button.
                editButton.setEnabled(true);
            }
        }
    }
    class FireListener implements ActionListener {
        @Override
		public void actionPerformed(ActionEvent e) {
            //This method can be called only if
            //there's a valid selection
            //so go ahead and remove whatever's selected.
            int index = list.getSelectedIndex();
            listModel.removeAllElements();
            APIshDataManager.urlUp.remove(index);
            APIshDataManager.requestType.remove(index);
            APIshDataManager.creationContainer.remove(index);
        	TreeMap<Integer, LinkedHashMap<String, String>> listMap = (TreeMap<Integer, LinkedHashMap<String, String>>) APIshDataManager.creationContainer.clone();
        	Set<Entry<Integer, LinkedHashMap<String, String>>> listMapEntrySet = listMap.entrySet();
        	int meow = 0;
    		APIshDataManager.creationContainer.clear();
        	for ( Entry<Integer, LinkedHashMap<String, String>> it : listMapEntrySet){
        		LinkedHashMap<String, String> itV = it.getValue();
        		APIshDataManager.creationContainer.put(meow, itV);
        		meow++;
        	}
            APIshCreatorLeftPanel.n = 0;
            for(int i = 0; i < (APIshDataManager.urlUp.size()); i++){
            	listConstructor(i);
            }
            APIshCreatorLeftPanel.n++;
            list.invalidate();
            list.repaint();
            list.validate();
            int size = listModel.getSize();

            if (size == 0) { //Nobody's left, disable firing.
                editButton.setEnabled(false);

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
			if (list.getSelectedIndex() != 0){
		        int indexOfSelected = list.getSelectedIndex();
		        swapElements(indexOfSelected, indexOfSelected - 1);
		        list.updateUI();
			}
		}
		private void swapElements(int pos1, int pos2) {
	        String tmp = (String) listModel.get(pos1);
	        LinkedHashMap<String, String> map1 = APIshDataManager.creationContainer.get(pos1);
	        LinkedHashMap<String, String> map2 = APIshDataManager.creationContainer.get(pos2);
	        APIshDataManager.creationContainer.put(pos1, map2);
	        APIshDataManager.creationContainer.put(pos2, map1);
	        listModel.set(pos1, listModel.get(pos2));
	        listModel.set(pos2, tmp);
	    }
    }
    class RunListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			APIshRunner.run();
		}
    }
}
