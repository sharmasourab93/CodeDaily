/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Collection;
import java.util.*;
/**
 *
 * @author esoussh
 */
public class PriorQue {
    public static void main(String[] args){
        PriorityQueue<String> pQueue=new PriorityQueue<>();
        pQueue.add("C");
        pQueue.add("C++");
        pQueue.add("java");
        pQueue.add("Python");
        
        System.out.println("Head value of by using peek "+pQueue.peek());
        Iterator iter=pQueue.iterator();
        while(iter.hasNext()){
            System.out.println(iter.next());
        }
        System.out.println(pQueue.contains("C"));
        //To convert a priority queue to an array
        Object array[]=pQueue.toArray();
    }
}
