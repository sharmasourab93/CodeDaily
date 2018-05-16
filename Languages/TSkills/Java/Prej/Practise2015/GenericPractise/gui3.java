package javaapp;
import java.awt.*;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.*;
import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
public class gui3 extends JFrame {
    private JTextField tf;
    private Font pf;
    private Font bf;
    private Font itf;
    private Font bif;
    private JRadioButton pb;
    private JRadioButton bb;
    private JRadioButton ib;
    private JRadioButton bib;
    private ButtonGroup group;//to keep all buttons jointlyor like a family
    
    public gui3(){
        super("The Title");
        setLayout(new FlowLayout());
        tf=new JTextField("Bucky is awesome",25);
        add(tf);
        pb=new JRadioButton("plain",true);
        bb=new JRadioButton("bold",false);
        ib=new JRadioButton("italic",false);
        bib=new JRadioButton("bold and italic",false);
        add(pb);
        add(bb);
        add(ib);
        add(bib);
        //grouped together
        group = new ButtonGroup();
        group.add(pb);
        group.add(bb);
        group.add(ib);
        group.add(bib);
        
        pf=new Font("Serif",Font.PLAIN,14);
        bf=new Font("Serif",Font.BOLD,14);
        itf=new Font("Serif",Font.ITALIC,14);
        bif=new Font("Serif",Font.BOLD+Font.ITALIC,14);
        tf.setFont(pf);
        //wait for event to happen and pass in font object to constructor
        pb.addItemListener(new HandlerClass(pf));
        bb.addItemListener(new HandlerClass(bf));
        ib.addItemListener(new HandlerClass(itf));
        bib.addItemListener(new HandlerClass(bif));                
    }
    
    private class HandlerClass implements ItemListener{
        private Font font;
        //the font object gets variable font
        public HandlerClass(Font f){
            font=f;
        }
        //sets the font to the font object that was passed in
        public void itemStateChanged(ItemEvent event){
            tf.setFont(font);
        }
    }
    
}
