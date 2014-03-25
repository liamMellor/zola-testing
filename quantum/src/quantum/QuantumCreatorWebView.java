package quantum;
import static javafx.concurrent.Worker.State.FAILED;

import java.awt.BorderLayout;
import java.awt.DefaultKeyboardFocusManager;
import java.awt.Dimension;
import java.awt.KeyEventDispatcher;
import java.awt.KeyboardFocusManager;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.net.MalformedURLException;
import java.net.URL;

import javafx.application.Platform;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.embed.swing.JFXPanel;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebEvent;
import javafx.scene.web.WebView;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

import org.w3c.dom.Document;

public class QuantumCreatorWebView implements Runnable {
    private JFXPanel jfxPanel;
    private WebEngine engine;

    private JFrame frame = new JFrame();
    private JPanel panel = new JPanel(new BorderLayout());
    private JLabel lblStatus = new JLabel();

    private JButton btnGo = new JButton("Go");
    private JTextField txtURL = new JTextField();
    private JProgressBar progressBar = new JProgressBar();

    public JFXPanel initComponents() {
        jfxPanel = new JFXPanel();
        jfxPanel.setPreferredSize(new Dimension(700,700));
        createScene();

        ActionListener al = new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                loadURL(txtURL.getText());
            }
        };
        KeyboardFocusManager kfm = DefaultKeyboardFocusManager.getCurrentKeyboardFocusManager();
        kfm.addKeyEventDispatcher(new KeyEventDispatcher() {

			@Override
			public boolean dispatchKeyEvent(KeyEvent e) {
				if (DefaultKeyboardFocusManager.getCurrentKeyboardFocusManager().getFocusOwner() == jfxPanel) {
	                if (e.getID() == KeyEvent.KEY_TYPED && e.getKeyChar() == 10) {
	                    e.setKeyChar((char) 13);
	                }
	                return false;
	             }
				return false;
			}
        });
        btnGo.addActionListener(al);
        QuantumStyleManager.buttonStyles(btnGo);
        txtURL.addActionListener(al);

        progressBar.setPreferredSize(new Dimension(150, 18));
        progressBar.setStringPainted(true);

        JPanel topBar = new JPanel(new BorderLayout(5, 0));
        topBar.setBorder(BorderFactory.createEmptyBorder(3, 5, 3, 5));
        topBar.add(txtURL, BorderLayout.CENTER);
        topBar.add(btnGo, BorderLayout.EAST);


        JPanel statusBar = new JPanel(new BorderLayout(5, 0));
        statusBar.setBorder(BorderFactory.createEmptyBorder(3, 5, 3, 5));
        statusBar.add(lblStatus, BorderLayout.CENTER);
        statusBar.add(progressBar, BorderLayout.EAST);

        panel.add(topBar, BorderLayout.NORTH);
        panel.add(jfxPanel, BorderLayout.CENTER);
        panel.add(statusBar, BorderLayout.SOUTH);

        frame.getContentPane().add(panel);
		return jfxPanel;
    }
    /**
     * Enables Firebug Lite for debugging a webEngine.
     * @param engine the webEngine for which debugging is to be enabled.
     */
    private static void enableFirebug(final WebEngine engine) {
      engine.executeScript("if (!document.getElementById('FirebugLite')){E = document['createElement' + 'NS'] && document.documentElement.namespaceURI;E = E ? document['createElement' + 'NS'](E, 'script') : document['createElement']('script');E['setAttribute']('id', 'FirebugLite');E['setAttribute']('src', 'https://getfirebug.com/' + 'firebug-lite.js' + '#startOpened');E['setAttribute']('FirebugLite', '4');(document['getElementsByTagName']('head')[0] || document['getElementsByTagName']('body')[0]).appendChild(E);E = new Image;E['setAttribute']('src', 'https://getfirebug.com/' + '#startOpened');}"); 
    }
    private static void enableXpath(final WebEngine engine) {
        engine.executeScript("function getXpath(e){var t=getPrevSibs(e);var n;if(getParentId(e)!=undefined){n=getParentId(e);var r=\"//*[@\"+'id=\"'+n+'\"]/'+e.tagName.toLowerCase()+\"[\"+t+\"]\";return r}else{n=getParentClass(e);var r=\"//*[@\"+'class=\"'+n+'\"]/'+e.tagName.toLowerCase()+\"[\"+t+\"]\";return r}}function getPrevSibs(e){var t=true;var n=0;while(t==true){var r;if(n==0){if(e.prevElementSibling!=undefined){r=e.prevElementSibling;if(r.tagName==e.tagName)n+=1}else{t=false;break}}else{if(r.prevElementSibling!=undefined){var i=r;r=r.prevElementSibling;if(i.tagName==r.tagName)n+=1}else{t=false;break}}}return n}function getParentId(e){var t=e.parentElement;var n=t.getAttribute(\"id\");return n}function getParentClass(e){var t=e.parentElement;var n=t.getAttribute(\"class\");return n}var el;document.oncontextmenu=function(e){el=e.toElement}"); 
      }
    public void createScene() {

        Platform.runLater(new Runnable() {
            @Override public void run() {

                final WebView view = new WebView();
                
                engine = view.getEngine();
                
                engine.titleProperty().addListener(new ChangeListener<String>() {
                    @Override
                    public void changed(ObservableValue<? extends String> observable, String oldValue, final String newValue) {
                        SwingUtilities.invokeLater(new Runnable() {
                            @Override public void run() {
                                frame.setTitle(newValue);
                            }
                        });
                    }
                });
                engine.documentProperty().addListener(new ChangeListener<Document>() {
                    @Override public void changed(ObservableValue<? extends Document> prop, Document oldDoc, Document newDoc) {
                      enableFirebug(engine);
                      enableXpath(engine);
                    }
                  });
                
                engine.setOnStatusChanged(new EventHandler<WebEvent<String>>() {
                    @Override public void handle(final WebEvent<String> event) {
                        SwingUtilities.invokeLater(new Runnable() {
                            @Override public void run() {
                                lblStatus.setText(event.getData());
                            }
                        });
                    }
                });

                engine.locationProperty().addListener(new ChangeListener<String>() {
                    @Override
                    public void changed(ObservableValue<? extends String> ov, String oldValue, final String newValue) {
                        SwingUtilities.invokeLater(new Runnable() {
                            @Override public void run() {
                                txtURL.setText(newValue);
                            }
                        });
                    }
                });
                engine.getLoadWorker().workDoneProperty().addListener(new ChangeListener<Number>() {
                    @Override
                    public void changed(ObservableValue<? extends Number> observableValue, Number oldValue, final Number newValue) {
                        SwingUtilities.invokeLater(new Runnable() {
                            @Override public void run() {
                                progressBar.setValue(newValue.intValue());
                            }
                        });
                    }
                });

                engine.getLoadWorker()
                        .exceptionProperty()
                        .addListener(new ChangeListener<Throwable>() {

                            public void changed(ObservableValue<? extends Throwable> o, Throwable old, final Throwable value) {
                                if (engine.getLoadWorker().getState() == FAILED) {
                                    SwingUtilities.invokeLater(new Runnable() {
                                        @Override public void run() {
                                            JOptionPane.showMessageDialog(
                                                    panel,
                                                    (value != null) ?
                                                    engine.getLocation() + "\n" + value.getMessage() :
                                                    engine.getLocation() + "\nUnexpected error.",
                                                    "Loading error...",
                                                    JOptionPane.ERROR_MESSAGE);
                                        }
                                    });
                                }
                            }
                        });
                Platform.setImplicitExit(false);

                jfxPanel.setScene(new Scene(view));
            }
        });
    }

    public void loadURL(final String url) {
        Platform.runLater(new Runnable() {
            @Override public void run() {
                String tmp = toURL(url);

                if (tmp == null) {
                    tmp = toURL("http://" + url);
                }

                engine.load(tmp);
            }
        });
    }

    private static String toURL(String str) {
        try {
            return new URL(str).toExternalForm();
        } catch (MalformedURLException exception) {
                return null;
        }
    }

    @Override
    public void run() {

        frame.setPreferredSize(new Dimension(700, 700));
        frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        initComponents();

        loadURL("http://oracle.com");

        frame.pack();
        frame.setVisible(true);
    }
    public void destroy(){

    	frame = new JFrame();
    }
    
}