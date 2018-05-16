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
public class HashTreeMap {
    static void printFreq(int arr[]){
        TreeMap<Integer,Integer> tmap=new TreeMap<>();
        for(int i=0;i<arr.length;i++){
            Integer c=tmap.get(arr[i]);
            //System.out.println(c);
            if(tmap.get(arr[i])==null){
                tmap.put(arr[i],1);
            }else{
                tmap.put(arr[i],++c);
            }
        }
        for(Map.Entry m:tmap.entrySet()){
            System.out.println("Frequency of "+m.getKey()+" is "+m.getValue());
        }
        System.out.println(tmap);
    }
    public static void main(String[] args){
        int arr[]={10,34,5,10,3,5,10};
        printFreq(arr);
    }
}
