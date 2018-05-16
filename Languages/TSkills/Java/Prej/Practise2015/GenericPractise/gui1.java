package javaapp;
import java.awt.FlowLayout;
import javax.swing.JFrame;//JFrame Gives you a all basic Windows features
import javax.swing.JLabel;//for outputting text and images
public class gui1 extends JFrame{
        private JLabel item1;
        public gui1(){
            super("The Title bar");//adds title
            setLayout(new FlowLayout());//default layout
            
            item1 =new JLabel("A Sentence");
            item1.setToolTipText("Hovering...");
            add(item1);
        }
    }   


   