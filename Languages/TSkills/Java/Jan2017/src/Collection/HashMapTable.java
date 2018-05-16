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
public class HashMapTable {
    public static void main(String[] args){
        Hashtable<Integer,String> ht=new Hashtable<>();
        ht.put(101, "Ajay");
        ht.put(102,"Vijay");
        ht.put(102,"Avijay");
        ht.put(103,"Jayy");
        ht.put(105,"Raul");
        System.out.println("Hashtable");
        //New way for functional operation
        ht.entrySet().forEach((m) -> {
            System.out.println(m.getKey()+" "+m.getValue());
        });
        HashMap<Integer,String> hm=new HashMap<>();
        hm.put(100, "Amit");
        hm.put(101, "Anjana");
        hm.put(104, "Lojay");
        hm.put(104, "Tamit");
        hm.put(100, "KAmit");
        System.out.println("HashMap");
        hm.entrySet().forEach((m) -> {
            System.out.println(m.getKey()+" "+m.getValue());
        });    
    }
}
