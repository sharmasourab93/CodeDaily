/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Swing;
import javax.swing.*;
/**
 *
 * @author esoussh
 */
public class ExtendJFrame extends JFrame{
    JFrame frame;
    ExtendJFrame(){
        setTitle("This is also a title");
        JButton button=new JButton("Don't Dare!");
        button.setBounds(10,10,10,10);
        add(button);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(100,100);
        setLayout(null);
        setVisible(false);
    }
    public static void main(String[] args) {
        new ExtendJFrame();
    }
}
