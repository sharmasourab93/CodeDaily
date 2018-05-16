/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Generics;

/**
 *
 * @author esoussh
 */
//We use < > to specify parameter type
class Test<T>{
   T obj;
   //Constructor
   Test(T obj){this.obj=obj;} 
   public T getObject() {return this.obj;}
}
//Driver class to test above
public class Main {
    public static void main(String[] args) {
        //Instance of Integer type
        Test<Integer> iObj=new Test<Integer>(15);
        System.out.println(iObj.getObject());
        //Instance of string type
        Test <String> sObj=new Test<String>("GeeksforGeeks");
        System.out.println(sObj.getObject());
    }
  
}
