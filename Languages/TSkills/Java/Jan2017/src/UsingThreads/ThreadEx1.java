/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UsingThreads;
//import java.lang.Thread;
/**
 *
 * @author esoussh
 */
class MultithreadingDemo extends Thread{
    @Override
    public void run(){
        try{
            System.out.println("Thread "+Thread.currentThread().getId()+ " is running");
        }
        catch(Exception e){
            System.out.println("Exception is caught");
        }
    }
}
public class ThreadEx1 {
    public static void main(String[] args){
        //int n=8;//Number of threads
        for(int i=0;i<8;i++){
            MultithreadingDemo object=new MultithreadingDemo();
            object.start();
        }
    }
}
