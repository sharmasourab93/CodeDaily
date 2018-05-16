package javaapp;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class gui9 extends JFrame{
    private JButton b;
    private Color color=(Color.WHITE);
    private JPanel panel;
    public gui9(){
        super("THe Title");
        panel=new JPanel();
        panel.setBackground(color);
        b=new JButton("CHoose a color");
        b.addActionListener(
                new ActionListener(){
                    public void actionPerformed(ActionEvent event){
                        color=JColorChooser.showDialog(null,"Pick your color",color);
                    
                        if(color==null)
                            color=(Color.WHITE);
                        panel.setBackground(color);
                    }
                }
        
                );
   
        add(panel,BorderLayout.CENTER);
        add(b,BorderLayout.SOUTH);
        setSize(425,150);
        setVisible(true);
    }

}
