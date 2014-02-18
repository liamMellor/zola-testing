package quantum;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileInputStream;

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
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class QuantumManagerCenterPanel {
	public static JList<String> list;
    public static DefaultListModel<String> listModel;

    private static final String moveLeftString = "Move Left";
    private static final String runString = "Run All";
    static JButton moveLeftButton;
    static JButton runButton;
	private FileInputStream inputStream;
	private JPanel centerPane;
	private QuantumManagerMain qMain;
	
	public QuantumManagerCenterPanel(JPanel centerPane, QuantumManagerMain quantumMain){
		this.centerPane = centerPane;
		this.qMain = quantumMain;
		
	}
    public JSplitPane QuantumTopCenter() {

        listModel = new DefaultListModel<String>();
        listModel.addElement("");
        //Create the list and put it in a scroll pane.
        list = new JList<String>(listModel);
        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
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
        listScrollPane.setPreferredSize(new Dimension(500, 250));
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
		                runButton.setEnabled(false);

		            } else {
		            //Selection, enable the fire button.
		                moveLeftButton.setEnabled(true);
		                runButton.setEnabled(true);
		            }
		        }
			}
        	
        });
        final JTextArea runnerConsole = consolePane();
        final JScrollPane consolePane = new JScrollPane(runnerConsole);
        consolePane.setVerticalScrollBarPolicy(
                        JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        consolePane.setPreferredSize(new Dimension(500,250));
        JSplitPane hopperAndConsole = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
        		listWithButtons,
        		consolePane);
		return hopperAndConsole;
    }
    private JTextArea consolePane() {
		JTextArea textArea = new JTextArea(
                QuantumDataManager.runnerConsole
        );
        textArea.setFont(new Font("Monospaced", Font.PLAIN, 16));
        textArea.setBackground(Color.black);
        textArea.setForeground(Color.GREEN);
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
    public static void listValueChanged(ListSelectionEvent e) {
        if (e.getValueIsAdjusting() == false) {

            if (list.getSelectedIndex() == -1) {
            //No selection, disable fire button.
                moveLeftButton.setEnabled(false);
                runButton.setEnabled(false);

            } else {
            //Selection, enable the fire button.
                moveLeftButton.setEnabled(true);
                runButton.setEnabled(true);
            }
        }
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
				QuantumRunner.reconstruct(constructorSetter);
				QuantumRunner.run();
			}
		}
    }
}
