/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Collection;
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.*;
/**
 *
 * @author esoussh
 */
public class AddingList {
    public static void main(String[] args){
        List l=new ArrayList();
        l.add(10);
        l.add(20);
        l.add("Strings");
        System.out.println("Iterating through ArrayList using for loop");
        for(Object o:l){
            System.out.println(o);
        }
        Iterator iter=l.iterator(),it=l.iterator();
        System.out.println("Using Iterator using Iterator");
        while(iter.hasNext()){
            Object ob=iter.next();
            System.out.println(ob);
        }
        /*while(it.hasPrevious()){
            Object ob=it.previous();
            System.out.println(ob);
        }*/
        
    }
}
