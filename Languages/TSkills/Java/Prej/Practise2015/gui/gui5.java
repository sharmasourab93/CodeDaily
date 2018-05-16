package javaapp;
import javax.swing.*;
import java.awt.*;
import javax.swing.event.*;
public class gui5 extends JFrame{
    private JList list;
    private static String[] colornames={"black","white","red","blue"};
    private static Color[] colors={Color.BLACK,Color.BLUE,Color.WHITE,Color.RED};
    
    public gui5(){
        super("The Title");
        setLayout(new FlowLayout());
        
        list = new JList(colornames);
        list.setVisibleRowCount(4);
        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        add(new JScrollPane(list));
        
        list.addListSelectionListener(
                new ListSelectionListener(){
                    public void valueChanged(ListSelectionEvent event){
                        getContentPane().setBackground(Color.yellow);
                    }
                }
        );
    }
}
