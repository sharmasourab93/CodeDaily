/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
class Fruit{
    public Fruit(){
        System.out.println("Super class Constructor");
        System.out.println("Super class object hash code "+this.hashCode());
        System.out.println(this.getClass().getName());
    }
}
//Sub class
class Apple extends Fruit{
    public Apple(){
        System.out.println("Subclass constructor invoked");
        System.out.println("Subclass object hashcode "+this.hashCode());
        System.out.println("Super class object hashcode "+super.hashCode());
        System.out.println(this.getClass().getName()+" "+super.getClass().getName());
    }
}
/**
 *
 * @author esoussh
 */
public class Test {
    public static void main(String[] args){
        Apple myApple=new Apple();
        System.out.println(myApple instanceof Apple);
    }
}
