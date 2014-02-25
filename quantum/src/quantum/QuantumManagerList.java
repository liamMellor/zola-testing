package quantum;

import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileFilter;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.List;

import javax.swing.BorderFactory;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.DefaultListCellRenderer;
import javax.swing.DefaultListModel;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSeparator;
import javax.swing.JSplitPane;
import javax.swing.ListSelectionModel;
import javax.swing.SwingConstants;
import javax.swing.border.Border;
import javax.swing.border.EmptyBorder;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.filechooser.FileSystemView;

import org.apache.commons.io.IOUtils;

public class QuantumManagerList {

    private static final String moveUpString = "Edit Test";
    private static final String moveDownString = "Add to Hopper";
    private static final String fireString = "Delete Test";
    static JButton fireButton;
    static JButton editorButton;
    static JButton moveRightButton;
	private static FileInputStream inputStream;
	private QuantumManagerMain qmMain;
	private static JPanel fileMain;
	static DefaultListModel<String> listModel = new DefaultListModel<String>();
	static JList fileFileList = new JList(listModel);

	
	public QuantumManagerList(QuantumManagerMain qmMain){
		this.qmMain = qmMain;
	}
    public JSplitPane QuantumList() {

        /*listModel = new DefaultListModel<String>();
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
        	
        });
        list.setVisibleRowCount(5);
        JScrollPane listScrollPane = new JScrollPane(list);*/

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
        //listScrollPane.setPreferredSize(new Dimension(400, 600));
        buttonPane.setPreferredSize(new Dimension(20, 20));
        FileList fl = new FileList();
        fileMain = fl.fileMain();
        JSplitPane listWithButtons = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
       	fileMain,
        buttonPane);
        
        fireButton.setEnabled(false);
        editorButton.setEnabled(false);
        moveRightButton.setEnabled(false);
        
		return listWithButtons;

    }
    
    class FireListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            //This method can be called only if
            //there's a valid selection
            //so go ahead and remove whatever's selected.
            int index = fileFileList.getSelectedIndex();
            fileFileList.remove(index);
            //QuantumDataManager.creationContainer.remove(index);
            int size = listModel.getSize();

            if (size == 0) { //Nobody's left, disable firing.
                fireButton.setEnabled(false);

            } else { //Select an index.
                if (index == listModel.getSize()) {
                    //removed item in last position
                    index--;
                }

                fileFileList.setSelectedIndex(index);
                fileFileList.ensureIndexIsVisible(index);
            }
        }
    }
    class EditorListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			File entryF = (File) fileFileList.getSelectedValue();
			String entry = entryF.getName();
			if(entry.contains(".qtm")){
				QuantumCreatorMain.createAndShowGUI(qmMain);
				String constructorSetter = QuantumDataManager.managerContainer.get(entry);
				QuantumConstructor.reconstruct(constructorSetter, true);
			}
			else if (entry.contains(".api")){
				APIshCreatorMain.createAndShowGUI(qmMain);
				String constructorSetter = QuantumDataManager.managerContainer.get(entry);
				APIshConstructor.reconstruct(constructorSetter, true);
			}
	    }
    }
    class MoveRightListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			List<File> selectedVals = fileFileList.getSelectedValuesList();
			String valName = null;
			for(File val : selectedVals)
				valName = val.getName();
				QuantumManagerCenterPanel.listModel.addElement(valName);
		}
    }
    static class FileList {
    	static JList dirFileList = new JList();
    	
        public static Component getGui(File[] all, boolean vertical) {
            // put File objects in the list..
            dirFileList = new JList(all);
            // ..then use a renderer
            dirFileList.setCellRenderer(new FileRenderer(!vertical));

            if (!vertical) {
                dirFileList.setLayoutOrientation(javax.swing.JList.HORIZONTAL_WRAP);
                dirFileList.setVisibleRowCount(-1);
            } else {
                dirFileList.setVisibleRowCount(9);
            }
            return new JScrollPane(dirFileList);
        }
        public static Component getGuiFiles(File[] all, boolean vertical) {
            // put File objects in the list..
        	fileFileList = new JList(all);
            // ..then use a renderer
        	fileFileList.setCellRenderer(new FileRenderer(!vertical));
        	fileFileList.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
            if (!vertical) {
            	fileFileList.setLayoutOrientation(javax.swing.JList.HORIZONTAL_WRAP);
            	fileFileList.setVisibleRowCount(-1);
            } else {
            	fileFileList.setVisibleRowCount(9);
            }
            fileFileList.addListSelectionListener(new ListSelectionListener() {

    			@Override
    			public void valueChanged(ListSelectionEvent e) {
    				// TODO Auto-generated method stub
    				//QuantumList.list.setSelectedIndex(QuantumList.listModel.size()-1);
    				fireButton.setEnabled(true);
    				moveRightButton.setEnabled(true);
    				editorButton.setEnabled(true);
    			}
            	
            });
            return new JScrollPane(fileFileList);
        }
        File f;
        FileList fl;
        JScrollPane c2;
		JPanel gui = new JPanel(new BorderLayout());
		Component c1;
        public JPanel fileMain() {
                    f = new File("QuantumScripts/");
                    fl = new FileList();
                    c1 = FileList.getGui(f.listFiles(new TextFileFilter()),true);

                    //f = new File(System.getPrmoperty("user.home"));
                    c2 = new JScrollPane();
                    dirFileList.addListSelectionListener(new ListSelectionListener(){

						@Override
						public void valueChanged(ListSelectionEvent e) {
							// TODO Auto-generated method stub
							File newF = new File(dirFileList.getSelectedValue().toString());
							Component c3 = FileList.getGuiFiles(newF.listFiles(new TextFileFilter()),false);
							//c2 = (JScrollPane) FileList.getGuiFiles(newF.listFiles(new TextFileFilter()),false);
							gui.removeAll();
							gui.add(c1,BorderLayout.WEST);
		                    gui.add(c3,BorderLayout.CENTER);
							gui.invalidate();
							gui.repaint();
							gui.validate();
						}
                    	
                    });
                    gui.add(c1,BorderLayout.WEST);
                    gui.add(c2,BorderLayout.CENTER);
                    c2.setPreferredSize(new Dimension(300,600));
                    gui.setBorder(new EmptyBorder(3,3,3,3));
                    return gui;
        }
    }

    static class TextFileFilter implements FileFilter {

        public boolean accept(File file) {
            // implement the logic to select files here..
            String everything = null;
            String name = file.getName().toLowerCase();
            if(!file.isDirectory()){
	        	try {
	        		inputStream = new FileInputStream(file);
					everything = IOUtils.toString(inputStream);
		            QuantumDataManager.managerContainer.put(name, everything);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
            }
            //return name.endsWith(".java") || name.endsWith(".class");
            listModel.addElement(name);
            return name.length()<20;
        }
    }

    static class FileRenderer extends DefaultListCellRenderer {

        /**
		 * 
		 */
		private static final long serialVersionUID = 3722813316336455323L;
		private boolean pad;
        private Border padBorder = new EmptyBorder(3,3,3,3);

        FileRenderer(boolean pad) {
            this.pad = pad;
        }

        @Override
        public Component getListCellRendererComponent(
            JList<?> list,
            Object value,
            int index,
            boolean isSelected,
            boolean cellHasFocus) {

            Component c = super.getListCellRendererComponent(
                list,value,index,isSelected,cellHasFocus);
            JLabel l = (JLabel)c;
            File f = (File)value;
            l.setText(f.getName());
            ImageIcon ouroBlue = QuantumCreatorMain.createImageIcon("images/ouro-blue.png",
                    "ouroblue");
            ImageIcon ouroRed = QuantumCreatorMain.createImageIcon("images/ouro-red.png",
                    "ourored");
            if(f.getName().contains(".api")){
            	l.setIcon(ouroBlue);
            }
            else if (f.getName().contains(".qtm")){
            	l.setIcon(ouroRed);
            }
            else{
            	l.setIcon(FileSystemView.getFileSystemView().getSystemIcon(f));
            }
            if (pad) {
                l.setBorder(padBorder);
            }

            return l;
        }
    }
}
