package applet;
//Init method
import java.applet.*;
import java.awt.*;
import javax.swing.*;
public class applet2 extends Applet{
    private double sum;
    public void init(){
        String fn=JOptionPane.showInputDialog("Enter first number");
        String sn=JOptionPane.showInputDialog("Enter sec number");
        
        double n1=Double.parseDouble(fn);
        double n2=Double.parseDouble(sn);
        sum= n1+n2;
        
    }
    public void paint(Graphics g){
        super.paint(g);
        g.drawString("The Sum is "+sum, 25, 30);
    }
}
