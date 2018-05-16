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
public class Swing1 {
    JFrame frame;
    Swing1(){
        //creating instance of JFrame with name frame
        frame=new JFrame("Swing method for the first time");
        //Creates instance of JButton
        JButton button=new JButton("Click Me");
        button.setBounds(350,100,100,100);
        //Close operation
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //adds button in JFrame
        frame.add(button);
        //sets 500 width and 600 height
        frame.setSize(500,200);
        //uses no layout managers
        frame.setLayout(null);
        //makes the frame visible
        frame.setVisible(true);
    }
    public static void main(String[] args){
        new Swing1();
    }
}
