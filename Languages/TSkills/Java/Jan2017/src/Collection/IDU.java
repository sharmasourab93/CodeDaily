/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Collection;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 *
 * @author esoussh
 */
public class IDU {
    public static void main(String [] args){
        Set<Integer> a = new HashSet<>();
        a.addAll(Arrays.asList(new Integer[] {1,2,3,4,8,9,0}));
        Set<Integer> b= new HashSet<>();
        b.addAll(Arrays.asList(new Integer[]{1,2,7,5,4,0,7,5}));
        //to find union
        Set<Integer> union=new HashSet<>(a);
        union.addAll(b);
        System.out.println("Union of the two set: "+union);
        
        //to find intersection
        Set<Integer> intersection=new HashSet<>(a);
        intersection.retainAll(b);
        System.out.println("Intersection of the set: "+intersection);
        
        //To find the symmetric difference
        Set<Integer> difference= new HashSet<>(a);
        difference.removeAll(b);
        System.out.println("Difference of the two sets: "+difference);
    }
}
