package javaapp;
import java.awt.*;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.*;
public class gui2 extends JFrame{
    
    private JTextField tf;
    private JCheckBox boldbox;
    private JCheckBox italicbox;
    
    public gui2(){
        super("the Title");
         setLayout(new FlowLayout());
         
         tf=new JTextField("This is a sentenc");
         tf.setFont(new Font("Serif",Font.PLAIN,14));
            add(tf);
            boldbox=new JCheckBox("bold");
            add(boldbox);
            italicbox=new JCheckBox("Italic");
            add(italicbox);
            
            HandlerClass handler=new HandlerClass();
            boldbox.addItemListener(handler);
            italicbox.addItemListener(handler);
         }

    
    private class HandlerClass implements ItemListener{
        public void itemStateChanged(ItemEvent event){
            Font font=null;
            if(boldbox.isSelected()&& italicbox.isSelected())
                font=new Font("Serif",Font.BOLD + Font.ITALIC,14);
            else if(boldbox.isSelected())
                font=new Font("Serif",Font.BOLD,14);
            else if(italicbox.isSelected())
                font=new Font("Serif",Font.ITALIC,14);
            else 
                font=new Font("Serif",Font.PLAIN,14);
            tf.setFont(null);
        }
}
}
        
       
        
        
