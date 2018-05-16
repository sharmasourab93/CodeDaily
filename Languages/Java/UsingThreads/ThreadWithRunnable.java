/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UsingThreads;

/**
 *
 * @author esoussh
 */
class MulthreadingDemo implements Runnable{
    public void run(){
        try{
            System.out.println("Thread "+Thread.currentThread().getId());
            
        }catch(Exception e){
            System.out.println("Exception is caught");
        }
    }
}
public class ThreadWithRunnable {
    public static void main(String[] args){
        int n=8;
        for(int i=0;i<n;i++){
            Thread object=new Thread(new MulthreadingDemo());
            object.start();
        }
    }
}
