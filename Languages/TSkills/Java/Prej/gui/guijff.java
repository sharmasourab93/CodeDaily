package gui;
import javax.swing.*;
import java.awt.*;
import java.util.*;
import javax.swing.event.*;
public class guijff extends JFrame{
    private JSlider slider;
    private guijf thepanel;
    public guijff(){
        super("Title");
        thepanel=new guijf();
        thepanel.setBackground(Color.orange);
        slider=new JSlider(SwingConstants.HORIZONTAL,0,200,10);
        slider.setMajorTickSpacing(10);
        slider.setPaintTicks(true);
        
        slider.addChangeListener(
            new ChangeListener(){
                public void stateChanged(ChangeEvent e){
                        thepanel.setD(slider.getValue());
                    }
                }
        );
        add(slider, BorderLayout.SOUTH);
        add(thepanel, BorderLayout.NORTH); 
    }
}
