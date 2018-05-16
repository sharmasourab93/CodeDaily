/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
//import java.net.
/**
 *
 * @author esoussh
 */
public class PrimClass {
    public static void main(String[] args) {
        int i=1;
        int j =2;
        
        PrimClass x=new PrimClass();
        int x1= x.modify(i);
        System.out.println(x1);
    }
    private int modify(int i){
        return i+10;
    }
}
