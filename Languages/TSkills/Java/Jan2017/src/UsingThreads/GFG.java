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
class Line{
    /*
    *   if multiple threads(trains) will try to 
    * access this unsynchronized method,
    * they all will get it. SO there is chance
    *that object's state will be corrupted.
    */
    synchronized public void getLine(){
        for(int i=0;i<3;i++){
            System.out.println(i+"\t"+Thread.currentThread().getId());
            try{
                Thread.sleep(400);
            }catch(Exception e){
                System.out.println(e);
            }
        }
    }
}
class Train extends Thread{
    //Reference to Line's object.
    Line line;
    Train(Line line){
        this.line=line;
    }
    public void run(){
        line.getLine();
    }
}
public class GFG {
    public static void main(String[] args) throws InterruptedException{
        //Object of line class this is shared
        //amoung threads
        Line Obj=new Line();
        //creating the threads that are 
        //sharing the same object
        Train train1=new Train(Obj);
        Train train2=new Train(Obj);
        train1.start();
        train2.start();
        train1.join();
        train2.join();
    }
}
