package javaapp;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
/**
 *
 * @author Sourab Sharma
 */
public class gui6 extends JFrame{
    private JList leftlist;
    private JList rightlist;
    private JButton movebutton;
    private static String[] food={"dal","rice","chapathi","kuruma"};
    
    public gui6(){
        super("Title");
        setLayout(new FlowLayout());
        leftlist=new JList(food);
        leftlist.setVisibleRowCount(3);
        leftlist.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        add(new JScrollPane(leftlist));
        movebutton= new JButton("Move -->");
        movebutton.addActionListener(
                new ActionListener(){
                    public void actionPerformed(ActionEvent event){
                        rightlist.setListData(leftlist.getSelectedValues());
                    }
                }
              );
        add(movebutton);
        rightlist=new JList();
        rightlist.setVisibleRowCount(3);
        rightlist.setFixedCellWidth(100);
        rightlist.setFixedCellHeight(15);
        rightlist.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        add(new JScrollPane(rightlist));
    
    }
    
}
