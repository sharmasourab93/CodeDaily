package javaapp;
import javax.swing.*;
import javax.swing.event.*;
import java.awt.*;
import java.awt.event.*;
public class prac1 extends JFrame{
    private JButton button,button1,button2;
    private JTextField textfield,textfield2;
    private JLabel label;
    private Container container;
    private JPanel panel;
    private int n1,n2,n3;
        public prac1(){
            //marks the title of the window in the title bar
            super("Programmed Window");
            System.out.println("\n\n\n");
            //sets layout
            setLayout(new FlowLayout());
            label=new JLabel();
            button=new JButton("press for one");
            //button.
            //container=getContentPane();
            //adds a textfield in the window
           /* textfield=new JTextField();
            textfield.getName();
            add(textfield);
            textfield2=new JTextField("Hey Now!");
            textfield2.getName();
            add(textfield2);*/
            button.addActionListener(
                     new ActionListener(){   
                   public void actionPerformed(ActionEvent ae){      
                            
                       label.setText((Integer.parseInt(textfield.getText())
                               +Integer.parseInt(textfield2.getText()))+" ");  
                       
                   }
        }
            );
            
        }
}
