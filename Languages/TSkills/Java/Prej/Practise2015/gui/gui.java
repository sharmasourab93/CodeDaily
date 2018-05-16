package javaapp;
import javax.swing.JOptionPane;
public class gui {
    public static void main(String args[]){
        String firstnumber= JOptionPane.showInputDialog("Enter your first number");
        String secnumber= JOptionPane.showInputDialog("Enter your second number");
        int num1=Integer.parseInt(firstnumber);
        int num2=Integer.parseInt(secnumber);
        int sum=num1+num2;
        JOptionPane.showMessageDialog(null,"The sum is "+sum,"the title",JOptionPane.PLAIN_MESSAGE);
    }
}
