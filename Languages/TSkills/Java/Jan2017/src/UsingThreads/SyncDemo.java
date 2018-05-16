/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UsingThreads;
import java.util.*;
import java.io.*;
/**
 *
 * @author esoussh
 */
//A class used to send a message
class Sender{
    public /*synchronized*/ void send(String msg){
      synchronized(this){
        System.out.println("Sending\t"+msg);
        try{
            Thread.sleep(1000);
        }catch(Exception e){
            System.out.println("Thread interrupted.");
        }
        System.out.println("\n"+msg+"Sent");
        }
    }
}
//Class for send a message using Threads
class ThreadedSend extends Thread{
    private String msg;
    private Thread t;
    Sender sender;
    
    //Receives a message object and a string 
    //message to be sent
    ThreadedSend(String m, Sender obj){
        msg=m;
        sender=obj;
    }
    public void run(){
        //Only one thread can send a message
        //at a time 
        synchronized(sender){
            //Synchronizing the snd object
            sender.send(msg);
        }
    }
}
//Driver class
class SyncDemo {
    public static void main(String args[]){
        Sender snd=new Sender();
        ThreadedSend s1=new ThreadedSend(" hi ", snd);
        ThreadedSend s2= new ThreadedSend("Bye ",snd);
        //Start two threades of threaded send type
       /* s1.start();
        s2.start();
        try{
            s1.join();
            s2.join();
        }catch(Exception e){
            System.out.println("Interrupted");
        }*/
       s1.start();
       s2.start();
       try{
           s1.join();
           s2.join();
       }catch(Exception e){
           System.out.println("Interrupted");
       }
    }
}
