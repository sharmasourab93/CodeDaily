package javaapp;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class gui7 extends JFrame{
    private String details;
    private JLabel statusbar;
    public gui7(){
        super("Tutle");
        statusbar=new JLabel("This is default");
        add(statusbar,BorderLayout.SOUTH);//will apppear at the otom of the screen
        addMouseListener(new Mouseclass());
        
    }
    private class Mouseclass extends MouseAdapter{
        public void mouseClicked(MouseEvent event){}
        details= String.format("You clicked %d", event.getClickCount());
        
        if(event.isMetaDown()){
            details+="With right mouse button";
                    
        }else if (event.isAltDown()){
            details+="Either center mouse ut ";
        }else
             details+="Either left mouse ut ";
             statusbar.setText(details);
    }
}