package javaapp;
import java.awt.FlowLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.JOptionPane;

public class eventhand extends JFrame{
    
    private JTextField item1;
    private JTextField item3;
    private JTextField item2;
    private JPasswordField pwdfield;
    
    public eventhand(){
        super("The Title");
        setLayout(new FlowLayout());
        
        item1=new JTextField(10);
        add(item1);
        
        item2 = new JTextField("Enter the text here");
        add(item2);
        
        item3=new JTextField("Uneditable",20);
        item3.setEditable(false);//becomes uneditale
        
        pwdfield= new JPasswordField("mypass");
        add(pwdfield);
        
        thehandler handler=new thehandler();
        item1.addActionListener(handler);
        item2.addActionListener(handler);
        item3.addActionListener(handler);
        pwdfield.addActionListener(handler);
    }

      
    private class thehandler implements ActionListener{
        public void actionPerformed(ActionEvent event){
            String string="";
            if(event.getSource()==item1){
                string=String.format("field 1:%s ",event.getActionCommand());
            }else if(event.getSource()==item2){
                string=String.format("field 2:%s ",event.getActionCommand());
        }else if(event.getSource()==item3){
                string=String.format("field 3:%s ",event.getActionCommand());
        }
        /*else if(event.getSource()=pwdfield){
        string=String.format("Password field is %s",event.getActionCommand());}*/
            
        JOptionPane.showMessageDialog(null, string);
        
        }
    }
}
