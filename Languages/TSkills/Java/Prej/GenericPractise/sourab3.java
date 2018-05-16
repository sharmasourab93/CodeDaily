package javaapp.intermediate;
import java.util.*;
public class sourab3 {
    public static void main(String args[]){
        //convert stuff aray to a list
        String[] stuff={"apple ","corn ","banana ","pineapple"};
        List<String> l1=Arrays.asList(stuff);
        ArrayList<String> list=new ArrayList<String>();
        list.add("Youtube ");
        list.add("Google ");
        list.add("Microsoft ");
        System.out.println("Before adding...");
        for(String x: list)
            System.out.printf("\n%s",x);
     
        Collections.addAll(list,stuff);  //Here the contents in stuff is transfered to list
      
      System.out.println("\nAfter adding...");
        for(String y: list)
            System.out.printf("\n%s",y);
      
        System.out.println("\n"+Collections.frequency(list,"apple"));
        boolean tof=Collections.disjoint(list,l1);
        System.out.println(tof);
    }
}
