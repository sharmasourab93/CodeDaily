package gui;
import javax.swing.*;
import java.awt.*;
import java.util.*;
public class guijf extends JPanel{
    
    private int d = 10;
    
    public void paint(Graphics g){
        super.paintComponent(g);
        g.fillOval(10, 10, d, d);
    }
    public void setD(int newD){
        d=(newD>=0 ? newD:10);
        repaint();//repaints the entire thing once again
    }
    public Dimension getPreferedSize(){
        return new Dimension(200,200);
    }
    public Dimension getMinimumSize(){
        return getPreferedSize();
    }
}
