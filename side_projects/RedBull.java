import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;

import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.KeyStroke;


@SuppressWarnings("serial")
public class RedBull extends JFrame {
	protected int sleepInMs = 250;
	protected float hue = 0.0f;
	protected long lastSleepChange = 0;
	
    public RedBull() {
    	// set full screen
        setUndecorated(true);
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        GraphicsDevice screen = ge.getScreenDevices()[0];
        screen.setFullScreenWindow(this);
        
        // hide the mouse
        setCursor(getToolkit().createCustomCursor(
        		new BufferedImage(1,1,BufferedImage.TYPE_INT_ARGB),
        		new Point(0,0), "invisible"));
        
        // exit on escape key
        ((JPanel)getContentPane()).registerKeyboardAction(
        		new ActionListener() { public void actionPerformed(ActionEvent e) {
						System.exit(0);
				}}, KeyStroke.getKeyStroke(KeyEvent.VK_ESCAPE, 0), JComponent.WHEN_IN_FOCUSED_WINDOW);
        
        // accelerate on + key
        ((JPanel)getContentPane()).registerKeyboardAction(
        		new ActionListener() { public void actionPerformed(ActionEvent e) {
						speedUp(25);
				}}, KeyStroke.getKeyStroke(KeyEvent.VK_ADD, 0), JComponent.WHEN_IN_FOCUSED_WINDOW);
        
        // decelerate on - key
        ((JPanel)getContentPane()).registerKeyboardAction(
        		new ActionListener() { public void actionPerformed(ActionEvent e) {
						slowDown(25);
				}}, KeyStroke.getKeyStroke(KeyEvent.VK_SUBTRACT, 0), JComponent.WHEN_IN_FOCUSED_WINDOW);
    }
    
    public void speedUp(int amount) {
    	sleepInMs-=amount;
		if (sleepInMs <= 0)
			sleepInMs = 25;
		lastSleepChange = System.currentTimeMillis();
    }
    
    public void slowDown(int amount) {
    	sleepInMs+=amount;
		if (sleepInMs > 1000)
			sleepInMs = 1000;
		lastSleepChange = System.currentTimeMillis();
    }
    
 
    public static void main(String argv[]) {
        RedBull frame = new RedBull();
        Graphics g = frame.getGraphics();
        g.setColor(new Color(255,0,0));
        
        while(true) {
        	frame.painNext();
        	frame.sleep();
        }
    }
    
    public void painNext() {
    	// loop over the HSV spectrum, varying the hue (color),
    	// and keeping the saturation and value to the maximum, for bright colors.
    	// you can speed/slow things up/down by changing the sleep value
    	hue += 0.01f;
    	if (hue >= 6.0f)
    		hue = 0.0f;
    	float rgb[] = HSVtoRGB(hue, 1.0f, 1.0f);
    	Color color = new Color(rgb[0],rgb[1],rgb[2]);
    	Graphics g = getGraphics();
    	g.setColor(color);
    	g.fillRect(0,0, getWidth(), getHeight());
    	
    	// changed speed in the last 3 seconds, display the speed
    	if (System.currentTimeMillis()-lastSleepChange < 1000) {
    		paintSleepDelay();
    	}
    }
    
    public void paintSleepDelay() {
    	Graphics g = getGraphics();
    	g.setColor(Color.BLACK);
    	g.setFont(new Font("Arial", Font.BOLD, 48));
    	g.drawString(String.valueOf(sleepInMs), 48, 53);
    }
    
    public void sleep() {
    	try {
			Thread.sleep(sleepInMs);
		} catch (InterruptedException e) {}
    }
    
    /**
     * Converts from the Hue Saturation Value color space to RGB.
     * Stolen from the web.
     * @param h is given on [0->6] or -1
     * @param s given on [0->1]
     * @param v given on [0->1]
     * @return RGB are each returned on [0->1]
     */
    public static float[] HSVtoRGB(float h, float s, float v)
	{
		// H is given on [0->6] or -1. S and V are given on [0->1]. 
		// RGB are each returned on [0->1]. 
		float m, n, f;
		int i; 

		float[] hsv = new float[3];
		float[] rgb = new float[3];

		hsv[0] = h;
		hsv[1] = s;
		hsv[2] = v;

		if(hsv[0] == -1) {rgb[0] = rgb[1] = rgb[2] = hsv[2];
							return rgb;  }
		i = (int)(Math.floor(hsv[0]));
		f = hsv[0] - i;
		if(i%2 == 0) f = 1 - f; // if i is even 
		m = hsv[2] * (1 - hsv[1]); 
		n = hsv[2] * (1 - hsv[1] * f); 
		switch (i) { 
		case 6: 
		case 0: rgb[0]=hsv[2]; rgb[1]=n; rgb[2]=m; break;
		case 1: rgb[0]=n; rgb[1]=hsv[2]; rgb[2]=m; break;
		case 2: rgb[0]=m; rgb[1]=hsv[2]; rgb[2]=n; break;
		case 3: rgb[0]=m; rgb[1]=n; rgb[2]=hsv[2]; break;
		case 4: rgb[0]=n; rgb[1]=m; rgb[2]=hsv[2]; break;
		case 5: rgb[0]=hsv[2]; rgb[1]=m; rgb[2]=n; break;
		} 

		return rgb;
		
	} 

}
