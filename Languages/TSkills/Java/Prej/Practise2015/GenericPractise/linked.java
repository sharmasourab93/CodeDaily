package javaapp.intermediate;
import java.util.*;
public class linked {
    public static void main(String args[]){
            String[] things={"apples","noobs","pwnage","bacon","goats"};
            List<String> list1=new LinkedList<String>();
            for(String x:things)
                list1.add(x);
            System.out.println(list1);
            String[] things2={"sausage","bacon","goats","harrypotter"};
            List<String> list2=new LinkedList<String>();
            for(String y:things2)
                list2.add(y);
            System.out.println(list2);
            list1.addAll(list2);
            System.out.println(list1);
            list2=null;
            System.out.println(list2);
            printMe(list1);
            removeStuff(list1,2,5);
            printMe(list1);
            reverseMe(list1);
    } 
    //printMe Method
    private static void printMe(List<String> l){
        for(String b: l)
            System.out.printf(" %s ", b);
        System.out.println();
    }
    //Removestuff
    private static void removeStuff(List<String> l, int from, int to){
        l.subList(from, to).clear();
        
    }
    
     //reverseMe
    private static void reverseMe(List<String> l){
        ListIterator<String> bobby =l.listIterator(l.size());
        while(bobby.hasPrevious())
            System.out.printf(" %s ", bobby.previous());
    }
}
