package threads;
import threads.treading;
import java.util.*;
public class newthread {
    public static void main(String args[]){
       Thread t1= new Thread(new treading("one"));
       Thread t2= new Thread(new treading("Two"));
       Thread t3= new Thread(new treading("Three"));
       Thread t4= new Thread(new treading("Four"));
       
       t1.start();
       t2.start();
       t3.start();
       t4.start();
       
    }
}
