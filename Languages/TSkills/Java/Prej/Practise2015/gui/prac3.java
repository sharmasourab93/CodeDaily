package javaapp;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.event.*;
public class prac3 extends JFrame{
    
        
    private JOptionPane op1,op2,op3,op4;
    private JTextField jtf1,jtf2,jtf3;
    private JFrame jf1,jf2,jf3;
    private JLabel jl1,jl2,jl3;
    public prac3(){
        super("To Calculate Arithmetic value");
        setLayout(new FlowLayout());        
        jl1=new JLabel("How are you?");
        jl1.setToolTipText("Hovering");
        add(jl1);
        String x=JOptionPane.showInputDialog("Enter a text");
        jtf1= new JTextField(x);
        add(jtf1);
        JOptionPane.showMessageDialog(null,"hey now "+x,"",JOptionPane.PLAIN_MESSAGE);
        
        
        //add(jtf1);
       // String x= JOptionPane.showInputDialog("Hello! Please enter an integer");
       // int num1=Integer.parseInt(x);
        //JOptionPane.showMessageDialog(null,"This is"+num1,"",JOptionPane.PLAIN_MESSAGE);
    } 
}
