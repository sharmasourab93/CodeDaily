package javaapp;
import java.io.File;
import java.util.*;
import java.lang.*;
import javax.swing.JFrame;
import java.awt.*;
import java.awt.event.ActionListener;
import javax.swing.JButton;

public class filex extends JFrame{
        
    public static void main(String[] args){    
       
        private JButton lb;
        private JButton cb;
        private JButton rb;
        private FlowLayout layout;
        private Container container;
        public filex(){
            super("The title");
            layout=new FlowLayout();
            container=getContentPane();
            setLayout(layout);
            lb=new JButton("left");
            add(lb);
            lb.addActionListener(
                    new ActionListener(){
                        public void actionPerformed(){
                            layout.setAlignment(FlowLayout.left);
                            layout.layoutContainer(container);
                            
                        }
                    
                    })
            );
        }
        
    }
}
