/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.lang.Math;
import java.util.Random;
/**
 *
 * @author esoussh
 */
public class SquareRoot {
    public static void main(String[] args) {
        double root=Math.sqrt(25);
        Random r= new Random();
        double x= r.nextInt(10);
        System.out.println(root);
        System.out.println(x);
        
        int x1=10,y1=5;
        x1=x1^y1;
        y1=x1^y1;
        x1=x1^y1;
        System.out.println(x1+" "+y1);
        
    }
}
