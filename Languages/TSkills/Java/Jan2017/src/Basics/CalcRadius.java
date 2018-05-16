/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.util.Scanner;

/**
 *
 * @author esoussh
 */
public class CalcRadius {
    public double calc(int radius){
        double pi=(22/7.0);
        System.out.println(pi);
        double area=pi*radius*radius;
        //System.out.println("\nArea of the given circle with radius "+radius+"\nArea: "+area);
        return area;
    }
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        System.out.println("Enter Radius ");
        CalcRadius x=new CalcRadius();
        int radius=scan.nextInt();
        double area=x.calc(radius);
        System.out.println("Area for the given radius is: "+area);
        //double area=calc(radius);
    }
}
