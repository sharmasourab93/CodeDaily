/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.io.*;
/**
 *
 * @author esoussh
 */
 class A implements Serializable{
     int i;
     String s;
     public A(int i, String s){
         this.i=i;
         this.s=s;
     }
 }
public class Serialization{
    public static void main(String[] args) 
            throws IOException, ClassNotFoundException{
        //Serializing 'a'
        A a=new A(20,"GeeksforGeeks");
        FileOutputStream fos=new FileOutputStream("xyz.txt");
        ObjectOutputStream oos=new ObjectOutputStream(fos);
        oos.writeObject(a);
        
        //De-Serializing 'a'
        FileInputStream fis=new FileInputStream("xyz.txt");
        ObjectInputStream ois=new ObjectInputStream(fis);
        A b=(A)ois.readObject();
        System.out.println(b.i+" "+b.s);
        
        //Closing streams
        oos.close();
        ois.close();
    }
}