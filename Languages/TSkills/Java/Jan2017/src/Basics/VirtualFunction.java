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
class Base{
    public static void show(){
        System.out.println("Base::show() called");
    }
}
class Derived extends Base{
    public static void show(){
        System.out.println("In show function of derived class");
        //super.show();
        System.out.println("Derived::show() called");
    }
}
public class VirtualFunction {
    public static void main(String[] args){
        
        Base b=new Derived();
        b.show();
        b=new Base();
        b.show();
    }
}
