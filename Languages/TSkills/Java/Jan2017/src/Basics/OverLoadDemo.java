/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
/**
 *
 * @author esoussh
 */

public class OverLoadDemo {
    void test(){
        System.out.print("No Arguments");
    }
    void test(int a){
        System.out.println("Has one integer Argument");
    }
    void test(int a, int b){
        System.out.println("Has two integer Arguments");
    }
    public static void main(String[] args){
        OverLoadDemo OLD=new OverLoadDemo();
        OLD.test();
        OLD.test(2);
        OLD.test(2,3);
        System.out.println("Hence Demonstrates Overloading Objects");
    }
    ArrayCopy x=new ArrayCopy();
}
