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
interface interface1{
    public final int var=9;
}
class CustEx implements interface1{
    int x=10,y=20;
    //public CustEx(int z){
      //  int a=z;
    //}
    //public CustEx(int a, int b){
    public CustEx(int a, int b){
      //  this(40);
        this.x=a*var;
        this.y=b*var;
        System.out.println("This is X: "+x+"\nThis is y: "+y);
    }
    
}
public class ConstructorExample {
    public static void main(String[] args){
        CustEx g=new CustEx(11,21);
        
    }
}
