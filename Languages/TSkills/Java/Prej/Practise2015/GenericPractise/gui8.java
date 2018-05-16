package javaapp;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class gui8 extends JFrame{
    
    private JButton lb;
    private JButton cb;
    private JButton rb;
    private FlowLayout layout;
    private Container container;
    
    public gui8(){
        super("THe Beast");
        layout=new FlowLayout();
        container=getContentPane();
        setLayout(layout);
        
        lb=new JButton("Left");
        add(lb);
        lb.addActionListener(
                new ActionListener(){
                    public void actionPerformed(ActionEvent event){
                        layout.setAlignment(FlowLayout.LEFT);
                        layout.layoutContainer(container);
                        
                    }
                    
                }  
        );
        cb=new JButton("Center");
        add(cb);
        cb.addActionListener(
                new ActionListener(){
                    public void actionPerformed(ActionEvent event){
                        layout.setAlignment(FlowLayout.CENTER);
                        layout.layoutContainer(container);
                        
                    }
                    
                }
                
        );
        rb=new JButton("Right");
        add(rb);
        rb.addActionListener(
                new ActionListener(){
                    public void actionPerformed(ActionEvent event){
                        layout.setAlignment(FlowLayout.RIGHT);
                        layout.layoutContainer(container);
                        
                    }
                    
                }
                
        );
    }
    
}
