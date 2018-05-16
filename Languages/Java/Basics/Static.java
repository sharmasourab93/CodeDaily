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
public class Static {
    static int i;
    static int j;
    static int k;
    public static void main(String[] args){
        System.out.println("Value before calling method: "+i);
        Static t=new Static();
        t.method();
        System.out.println("Value after calling method: "+i);
        t.method();
        System.out.println("Value after calling method: "+i);
        t.method();
        System.out.println("Value after calling method: "+i);
        t.method();
        System.out.println("Value after calling method: "+i);
    }
    void method(){
        i++;k++;j++;
    }
}
