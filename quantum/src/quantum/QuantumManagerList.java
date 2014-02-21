package quantum;

import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

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

import org.apache.commons.io.IOUtils;

public class QuantumManagerList {
	static JList<String> list;
    static DefaultListModel<String> listModel;

    private static final String moveUpString = "Editor";
    private static final String moveDownString = "Move Right";
    private static final String fireString = "Delete";
    static JButton fireButton;
    static JButton editorButton;
    static JButton moveRightButton;
	private FileInputStream inputStream;
	private QuantumManagerMain qmMain;
	
	public QuantumManagerList(QuantumManagerMain qmMain){
		this.qmMain = qmMain;
	}
    public JSplitPane QuantumList() {

        listModel = new DefaultListModel<String>();
        listModel.addElement("");
        final File epochFolder = new File("QuantumScripts/epoch/");
        if (epochFolder.exists() || epochFolder.mkdirs()) {
        	listFilesForFolder(epochFolder);
        }
        if(QuantumDataManager.managerContainer.size() != 0){
        	listModel.remove(0);
        }
        //Create the list and put it in a scroll pane.
        list = new JList<String>(listModel);
        list.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        //list.setSelectedIndex(0);
        /*list.addListSelectionListener(new ListSelectionListener(){

			@Override
			public void valueChanged(ListSelectionEvent e) {
				// TODO Auto-generated method stub
			}
        	
        });*/
        list.setVisibleRowCount(5);
        JScrollPane listScrollPane = new JScrollPane(list);

        //HireListener hireListener = new HireListener(hireButton);
        //hireButton.setActionCommand(hireString);
        //hireButton.addActionListener(hireListener);

        fireButton = new JButton(fireString);
        fireButton.setActionCommand(fireString);
        fireButton.addActionListener(new FireListener());
        
        editorButton = new JButton(moveUpString);
        editorButton.setActionCommand(moveUpString);
        editorButton.addActionListener(new EditorListener());
        
        moveRightButton = new JButton(moveDownString);
        moveRightButton.setActionCommand(moveDownString);
        moveRightButton.addActionListener(new MoveRightListener());
        
        QuantumStyleManager.buttonStyles(editorButton, fireButton, moveRightButton);
        JPanel buttonPane = new JPanel();
        buttonPane.setLayout(new BoxLayout(buttonPane,
                                           BoxLayout.LINE_AXIS));
        buttonPane.add(fireButton);
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(new JSeparator(SwingConstants.VERTICAL));
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(editorButton);
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(new JSeparator(SwingConstants.VERTICAL));
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(moveRightButton);
        
        
        buttonPane.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
        listScrollPane.setPreferredSize(new Dimension(400, 600));
        buttonPane.setPreferredSize(new Dimension(20, 20));
        JSplitPane listWithButtons = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        listScrollPane,
        buttonPane);
        
        fireButton.setEnabled(false);
        editorButton.setEnabled(false);
        moveRightButton.setEnabled(false);
        
		return listWithButtons;

    }
    public void listFilesForFolder(final File folder) {
        for (final File fileEntry : folder.listFiles()) {
            if (fileEntry.isDirectory()) {
                listFilesForFolder(fileEntry);
            } else {
            	try {
                inputStream = new FileInputStream(fileEntry);
                
                String everything = IOUtils.toString(inputStream);
                QuantumDataManager.managerContainer.put(fileEntry.getName(), everything);
                listModel.addElement(fileEntry.getName());
                } catch (IOException e) {
					// TODO Auto-generated catch block
					break;
				} finally {
                    try {
						inputStream.close();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						break;
					}
                }
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
            //QuantumDataManager.creationContainer.remove(index);
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
			String entry = list.getSelectedValue();
			QuantumCreatorMain.createAndShowGUI(qmMain);
			String constructorSetter = QuantumDataManager.managerContainer.get(entry);
			QuantumConstructor.reconstruct(constructorSetter, true);
	    }
    }
    class MoveRightListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			QuantumManagerCenterPanel.listModel.addElement(list.getSelectedValue());
		}
    }
}
