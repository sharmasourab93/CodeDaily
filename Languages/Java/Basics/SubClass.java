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
 class MethodOverriding {
    public void show(){
      //super.show();
      System.out.println("This is the parent class");
  }  
}
public class SubClass extends MethodOverriding{
    public void show(){
        super.show();
        System.out.println("This is the sub class");
    }
    public static void main(String[] args){
        MethodOverriding x=new SubClass();//new SubClass();
        x.show();
    }
}
