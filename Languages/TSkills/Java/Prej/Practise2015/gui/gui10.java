package javaapp;
import javax.swing.*;
import java.awt.*;
import javax.swing.JFrame;

public class gui10 extends JPanel{
    public void paintComponent(Graphics g){
        super.paintComponents(g);
        this.setBackground(Color.WHITE);
        g.setColor(Color.BLUE);
        g.drawLine(10,10,50,100);
        
        g.setColor(Color.RED);
        g.drawRect(10,55,100,30);
        
        g.setColor(Color.GREEN);
        g.fillOval(10,95,100,30);
        
        
        g.setColor(Color.ORANGE);
        g.fill3DRect(10, 160, 100, 50, true);
    }

}
