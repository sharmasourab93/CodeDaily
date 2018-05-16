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
public class UsingSetSort {
    public static void main(String[] args){
        Set<String> hash_set=new HashSet<String>();
        hash_set.add("Ambika");
        hash_set.add("Avantika");
        hash_set.add("Ashwika");
        hash_set.add("Ashwika");
        hash_set.add("Anuska");
        hash_set.add("Anna");
        hash_set.add("Anna");
        System.out.println("Set output without the duplicates");
        System.out.println(hash_set);
        System.out.println("Sorted set after passing into Tree set");
        Set<String> tree_set=new TreeSet<String>(hash_set);
        System.out.println(tree_set);
        
        
        
    }
}
