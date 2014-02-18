package quantum;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.Collections;

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
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.SwingConstants;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class QuantumCreatorList {
	
	static JList list;
    static DefaultListModel listModel;

    private static final String moveUpString = "Move Up";
    private static final String moveDownString = "Move Down";
    private static final String fireString = "Remove";
    static JButton fireButton;
    static JButton moveUpButton;
    static JButton moveDownButton;
    
    public JSplitPane QuantumList() {

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

        fireButton = new JButton(fireString);
        fireButton.setActionCommand(fireString);
        fireButton.addActionListener(new FireListener());
        
        moveUpButton = new JButton(moveUpString);
        moveUpButton.setActionCommand(moveUpString);
        moveUpButton.addActionListener(new MoveUpListener());
        
        moveDownButton = new JButton(moveDownString);
        moveDownButton.setActionCommand(moveDownString);
        moveDownButton.addActionListener(new MoveDownListener());
        
        QuantumStyleManager.buttonStyles(fireButton,moveUpButton,moveDownButton);

        //employeeName.addActionListener(hireListener);
        //employeeName.getDocument().addDocumentListener(hireListener);
        String name = listModel.getElementAt(
                              list.getSelectedIndex()).toString();

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
        buttonPane.add(moveDownButton);
        buttonPane.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
        listScrollPane.setPreferredSize(new Dimension(400, 560));
        buttonPane.setPreferredSize(new Dimension(20, 20));
        JSplitPane listWithButtons = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        listScrollPane,
        buttonPane);
        listModel.removeAllElements();
        fireButton.setEnabled(false);
        moveUpButton.setEnabled(false);
        moveDownButton.setEnabled(false);
		return listWithButtons;

        //add(listScrollPane, BorderLayout.CENTER);
        //add(buttonPane, BorderLayout.PAGE_END);
    }
    public static void listAdder(String[] sa){
    	String constructedString = "Tag: "
	    + sa[0]+" "
	    + "Identifier Type: "
	    + sa[1]+" "
	    + "Identifier: "
	    + sa[2]+" "
	    + "Action: "
	    + sa[3];
    	listModel.addElement(constructedString);
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
            QuantumDataManager.creationContainer.remove(index);
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
    class MoveUpListener implements ActionListener {

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
	        Collections.swap(QuantumDataManager.creationContainer, pos1, pos2);
	        listModel.set(pos1, listModel.get(pos2));
	        listModel.set(pos2, tmp);
	    }
    }
    class MoveDownListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			if (list.getSelectedIndex() != (listModel.size() -1)){
		        int indexOfSelected = list.getSelectedIndex();
		        swapElements(indexOfSelected, indexOfSelected + 1);
		        list.updateUI();
			}
		}
		private void swapElements(int pos1, int pos2) {
	        String tmp = (String) listModel.get(pos1);
	        Collections.swap(QuantumDataManager.creationContainer, pos2, pos1);
	        listModel.set(pos1, listModel.get(pos2));
	        listModel.set(pos2, tmp);
	    }
    }
}
