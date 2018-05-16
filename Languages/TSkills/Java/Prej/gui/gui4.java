package javaapp;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
public class gui4 extends JFrame{
    private JComboBox box;
    private JLabel picture;
    private static String[] filename={"b.png","x.png"};
    private Icon[] pics={new ImageIcon(getClass().getResource(""))};
    
    public gui4(){
    
        super();
        setLayout(new FlowLayout());
        
        box=new JComboBox(filename);
        box.addItemListener(
                new ItemListener(){
                    public void itemStateChanged(ItemEvent event){
                        if(event.getStateChange()==ItemEvent.SELECTED)
                            picture.setIcon(pics[box.getSelectedIndex()]);
                    }
                }
        );
        add(box);
        picture=new JLabel(pics[0]);
        
    }
}
