/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Collection;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;
/**
 *
 * @author esoussh
 */
public class UsingSet {
    static int i;
    public static void main(String[] args){
        Set<Integer> s=new HashSet<>();
        System.out.println("Is the set empty?"+s.isEmpty());
        System.out.println("Adding elements to set");
            for(int m=0;m<5;m++){
                s.add(m);
            }
            System.out.println("All Elements added.Now iterating with Iterator");
            Iterator iter=s.iterator(), it=s.iterator();
                while(iter.hasNext()){
                    Object o=iter.next();
                    System.out.println(o);
                }
        //Converts a hashset to an array in a single line
        Integer count[]=s.toArray(new Integer[s.size()]);
        System.out.println("After converting the entire set to array");
        for(int o:count){
            i=i++;
            System.out.println("Index of the count"+i+"\t Value at the index"+o);
        }
        s.remove(0);
        //Set<Integer> s1=new HashSet<>();
        System.out.println("After removing 0 from the set, these are the objects");
        for(Object object:s){
            System.out.println(object);
        }    
    }
        
}
