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
public class LinkeList {
    public static void main(String args[]){
        //Creating object of class linkedlist
        LinkedList<String> object=new LinkedList<String>();
        object.add("A");
        object.add("B");
        object.addFirst("C");
        object.addLast("D");
        object.add("G");
        System.out.println("Linked list: "+object);
        
        //removing elements from the linked list
        object.remove("B");
        object.removeFirst();
        object.removeLast();
        System.out.println("linked list after deletion "+object);
        
        //Finding if element exists in the list or not
        boolean status=object.contains("E");
        if(status){
            
            System.out.println("Object exists");
        }
        else{
            
            System.out.println("Object doesn't exist");
        }
        //Number of elements in linked list
       // Object element=object.get(2);
        //object.set(2);
        System.out.println("Linked List after change: "+object);
        
    }
}
