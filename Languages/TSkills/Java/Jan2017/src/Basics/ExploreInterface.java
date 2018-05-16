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
class TestInteface{
    interface Test2{
        int square(int a);
    }   
}
class Exp1 implements TestInteface.Test2{
    @Override
    public int square(int a){
       return a*a;
    }
}
public class ExploreInterface extends Exp1 {
    ExploreInterface(){
        int y=super.square(11);
        int x=this.square(10);
        System.out.println("\n hail from the constructure!"+x+"\n And from the Super call "+y);
    }
    @Override
    public int square(int a){
       return a*a*a;
    }
    public static void main(String[] args){
        int a = 20;
        ExploreInterface e=new ExploreInterface();
        Exp1 ex=new Exp1();
        int cu=ex.square(a);
        int sq=e.square(a);
        System.out.println("Printing the square of"+a+" which is "+sq+"\n"
                + " And as per the Exp1 class "+cu);
         }
    
}
