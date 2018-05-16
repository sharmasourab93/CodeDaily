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
abstract class MyAbstractClass{
    abstract void MyAbstractFun();
    void fun(){
        System.out.println("In myAbstractClass fun()");
    }
}
public class Abstract extends MyAbstractClass{
    public void MyAbstractFun(){
        System.out.println("Hello! MyAbstractFun from MyAbstractClass");
    }
    public void fun(){
        super.fun();
        System.out.println("In ABstract's Fun");
    }
    public static void main(String[] args){
        Abstract x=new Abstract();
        x.MyAbstractFun();
        x.fun();
        //Class c=new Class();
        
    }
}
