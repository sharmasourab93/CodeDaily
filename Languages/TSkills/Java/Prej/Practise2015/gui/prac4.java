//To Create an Event handling Class in Java
package javaapp;
import javax.swing.*;
import javax.swing.event.*;
import java.awt.*;
import java.awt.event.*;
public class prac4 extends JFrame{
    private JFrame jf1;
    private JTextField jtf1,jtf2,jtf3;
    private JOptionPane op;
    private JButton jb;
    private JLabel jl1,jl2;
    private Container container;
    private JMenuBar greenMenuBar;
    public prac4(){
        
        super("Working with Java");
        jl1=new JLabel("Enter a Number");
        add(jl1);
        jtf1=new JTextField("Enter the text Here");
        ActionListener handler = null;
        jtf1.addActionListener(handler);
        add(jtf1);
        jtf1.setEditable(true);
        
        
    }

    private abstract class thehandler implements ActionListener{
        public void ActionListener(ActionEvent event){
            String num2;
            if(event.getSource()==jtf1){
                //num2=Integer.parseInt(jtf1);
                num2=String.format("Textfield 1 %s",event.getActionCommand());
                JOptionPane.showMessageDialog(null,"The Entered text is"+num2);
            }
        }
    }
}
