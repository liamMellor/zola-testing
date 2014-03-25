package quantum;

import java.awt.Color;
import java.awt.Component;
import java.awt.Font;
import java.awt.FontFormatException;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.GraphicsEnvironment;
import java.awt.Rectangle;
import java.awt.RenderingHints;
import java.awt.Shape;
import java.awt.font.FontRenderContext;
import java.awt.font.TextLayout;
import java.awt.geom.AffineTransform;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;

import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.plaf.ComboBoxUI;
import javax.swing.plaf.basic.BasicArrowButton;
import javax.swing.plaf.basic.BasicComboBoxUI;

public class QuantumStyleManager {
	public static Font mightyFont(){
		Font myFont = null;
		InputStream fontStream = null;
    	try {
    		fontStream =QuantumStyleManager
                      		 .class
                       		 .getResourceAsStream("fonts/dinengschrift.ttf");
             myFont = Font.createFont(Font.TRUETYPE_FONT, 
            		 fontStream);
             myFont = myFont.deriveFont(Font.BOLD,20);
             GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
             ge.registerFont(myFont);
    	 }	catch (MalformedURLException e1) {
	         // TODO Auto-generated catch block
	         e1.printStackTrace();
	     } catch (FontFormatException e) {
	         // TODO Auto-generated catch block
	         e.printStackTrace();
	     } catch (IOException e) {
	         // TODO Auto-generated catch block
	         e.printStackTrace();
	     }
    	finally{
    		try {
				fontStream.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	}
    	return myFont;
	}
	public static void buttonStyles(JButton... thatButton){
		for(JButton thisButton: thatButton){
			thisButton.setFont(mightyFont());
			thisButton.setBackground(Color.RED);
			thisButton.setForeground(Color.WHITE);
			thisButton.setAlignmentX( Component.CENTER_ALIGNMENT );//0.0
		}
	}
	static class FontPanel extends JPanel {
		  /**
		 * 
		 */
		private static final long serialVersionUID = -8404192986141274893L;

		public void paintComponent(Graphics g) {
		    super.paintComponent(g);
		    setBackground(Color.white);
		    int width = getSize().width;
		    int height = getSize().height;
		    Graphics2D g2 = (Graphics2D) g;

		    g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
		        RenderingHints.VALUE_ANTIALIAS_ON);

		    g2.setRenderingHint(RenderingHints.KEY_RENDERING,
		        RenderingHints.VALUE_RENDER_QUALITY);

		    FontRenderContext frc = g2.getFontRenderContext();
		    Font f = new Font("Helvetica", 1, 60);
		    String s = new String("Java Source and Support.");
		    TextLayout textTl = new TextLayout(s, f, frc);
		    AffineTransform transform = new AffineTransform();
		    Shape outline = textTl.getOutline(null);
		    Rectangle outlineBounds = outline.getBounds();
		    transform = g2.getTransform();
		    transform.translate(width / 2 - (outlineBounds.width / 2), height / 2
		        + (outlineBounds.height / 2));
		    g2.transform(transform);
		    g2.setColor(Color.blue);
		    g2.draw(outline);
		    g2.setClip(outline);
		  }
		}

	static class ColorArrowUI extends BasicComboBoxUI {

	    public static ComboBoxUI createUI(JComponent c) {
	        return new ColorArrowUI();
	    }

	    @Override protected JButton createArrowButton() {
	        return new BasicArrowButton(
	            BasicArrowButton.SOUTH,
	            Color.red, Color.black,
	            Color.white, Color.black);
	    }
	}
}
