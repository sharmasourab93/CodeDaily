/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UsingThreads;
import java.util.Scanner;
/**
 *
 * @author esoussh
 */
class ThreadTest extends Thread{
    public void run(){
        try{
            System.out.println("Thread "+Thread.currentThread().getId()+" is running");
        }
        catch(Exception e){
            //Throwing an exception
            System.out.println("Exception is caught");
        }
    }
}
//main Class
public class AnotherThread {
    public static void main(String[] args) {
        int n=8;
        for(int i=0;i<n;i++){
            ThreadTest object=new ThreadTest();
            //start() is replaced with run() for 
            //seeing the purpose of start
            object.run();
        }
    }
}