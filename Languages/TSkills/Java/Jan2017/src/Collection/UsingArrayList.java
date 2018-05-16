/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Collection;
import java.util.*;
//import java.lang.Integer;
/**
 *
 * @author esoussh
 */
public class UsingArrayList {
    public static void main(String[] args){
        ArrayList<Integer> arr=new ArrayList<>();
        int array[]={1,7,89,23,45,6,7,12};
        //arr.add(array);
        arr.add(20);
        arr.add(32);
        for(Object m:arr){
            System.out.println(m);
        }
        System.out.println(arr.contains(20));
        Integer Tarr[]=arr.toArray(new Integer[arr.size()]);
        System.out.println("After converting entire ArrayList to Array ");
        int i=Tarr.length;
        for(int j=0;j<i;j++){
            System.out.println(Tarr[j]);
        }   
    }
}
