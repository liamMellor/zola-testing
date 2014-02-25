package quantum;

import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

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
import javax.swing.JTextArea;
import javax.swing.ListSelectionModel;
import javax.swing.SwingConstants;
import javax.swing.border.TitledBorder;
import javax.swing.event.ListDataEvent;
import javax.swing.event.ListDataListener;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class QuantumManagerCenterPanel {
	public static JList<String> list;
    public static DefaultListModel<String> listModel;

    private static final String moveLeftString = "Remove From Hopper";
    private static final String runString = "Run All";
    static JButton moveLeftButton;
    static JButton runButton;
	private JTextArea terminal;
	
	public QuantumManagerCenterPanel(JPanel centerPane, QuantumManagerMain quantumMain){
		
	}
    public JSplitPane QuantumTopCenter() {

        listModel = new DefaultListModel<String>();
        listModel.addElement("");
        //Create the list and put it in a scroll pane.
        list = new JList<String>(listModel);
        list.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        list.setSelectedIndex(0);
        /*list.addListSelectionListener(new ListSelectionListener(){

			@Override
			public void valueChanged(ListSelectionEvent e) {
				// TODO Auto-generated method stub
			}
        	
        });*/
        list.setVisibleRowCount(5);
        JScrollPane listScrollPane = new JScrollPane(list);


        moveLeftButton = new JButton(moveLeftString);
        moveLeftButton.setActionCommand(moveLeftString);
        moveLeftButton.addActionListener(new MoveLeftListener());
        
        runButton = new JButton(runString);
        runButton.setActionCommand(runString);
        runButton.addActionListener(new RunListener());
        
        QuantumStyleManager.buttonStyles(moveLeftButton, runButton);
        
        JPanel buttonPane = new JPanel();
        buttonPane.setLayout(new BoxLayout(buttonPane,
                                           BoxLayout.LINE_AXIS));
        buttonPane.add(moveLeftButton);
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(new JSeparator(SwingConstants.VERTICAL));
        buttonPane.add(Box.createHorizontalStrut(5));
        buttonPane.add(runButton);
        
        
        buttonPane.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
        listScrollPane.setPreferredSize(new Dimension(700, 250));
        buttonPane.setPreferredSize(new Dimension(20, 20));
        JSplitPane listWithButtons = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        listScrollPane,
        buttonPane);
        //listModel.removeAllElements();
        moveLeftButton.setEnabled(false);
        runButton.setEnabled(false);
        list.addListSelectionListener(new ListSelectionListener(){
			@Override
			public void valueChanged(ListSelectionEvent e) {
				// TODO Auto-generated method stub
				
				if (e.getValueIsAdjusting() == false) {
		            if (list.getSelectedIndex() == -1) {
		            //No selection, disable fire button.
		                moveLeftButton.setEnabled(false);
		            } else {
		            //Selection, enable the fire button.
		                moveLeftButton.setEnabled(true);
		            }
		        }
			}
        	
        });
        listModel.addListDataListener(new ListDataListener(){

			@Override
			public void intervalAdded(ListDataEvent e) {
				// TODO Auto-generated method stub
				runButton.setEnabled(true);
			}

			@Override
			public void intervalRemoved(ListDataEvent e) {
				// TODO Auto-generated method stub
				if(listModel.size() < 1)
					runButton.setEnabled(false);
			}

			@Override
			public void contentsChanged(ListDataEvent e) {

			}
        	
        });
        listWithButtons.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createTitledBorder(listWithButtons.getBorder(),"Hopper",TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
                BorderFactory.createEmptyBorder(5,5,5,5)));
        final JTextArea runnerConsole = consolePane();
        final JScrollPane consolePane = new JScrollPane(runnerConsole);
        consolePane.setVerticalScrollBarPolicy(
                        JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        consolePane.setPreferredSize(new Dimension(980,250));
        consolePane.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createTitledBorder(consolePane.getBorder(),"Console",TitledBorder.CENTER, TitledBorder.TOP, QuantumStyleManager.mightyFont()),
                BorderFactory.createEmptyBorder(5,5,5,5)));
        JSplitPane hopperAndConsole = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        		listWithButtons,
        		consolePane);
        list.removeAll();
        listModel.removeAllElements();
		return hopperAndConsole;
    }
    private JTextArea consolePane() {
		terminal = new JTextArea(
                QuantumDataManager.runnerConsole
        );
		terminal.setPreferredSize(new Dimension(1000, 250));
		terminal.setMinimumSize(new Dimension(1000, 250));
		terminal.setSize(new Dimension(1000, 250));

		terminal.setFont(new Font("Monospaced", Font.PLAIN, 16));
		terminal.setLineWrap(true);
		terminal.setWrapStyleWord(true);
        JScrollPane areaScrollPane = new JScrollPane(terminal);
        areaScrollPane.setVerticalScrollBarPolicy(
                        JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        areaScrollPane.setPreferredSize(new Dimension(1000, 250));
        areaScrollPane.setBorder(
            BorderFactory.createCompoundBorder(
                BorderFactory.createCompoundBorder(
                                BorderFactory.createTitledBorder("Console"),
                                BorderFactory.createEmptyBorder(5,5,5,5)),
                areaScrollPane.getBorder()));
	    return terminal;
    }
    class MoveLeftListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			listModel.remove(list.getSelectedIndex());
		}
    }
    class RunListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			for(int i = 0; i < listModel.size()-1; i++){
				String entry = listModel.get(i+1).toString();
				String constructorSetter = QuantumDataManager.managerContainer.get(entry);
				if (entry.contains(".qtm")){
					QuantumConstructor.reconstruct(constructorSetter, false);
					QuantumRunner.run();
				}
				else{
					APIshConstructor.reconstruct(constructorSetter, false);
					APIshRunner.run();
				}
			}
		}
    }
}
