package datastructures;
import java.util.*;
public class llist {
    public static void main(String[] args){
        String[] things={"apples","noobs","pawnage","bacon","goats"};
        List<String> list1=new LinkedList<String>();
        for(String x: things)
            list1.add(x);
        
        String[] things2={"Sausage","bacon","goats","harrypotter"};
        List<String> list2=new LinkedList<String>();
        for(String y: things2)
            list2.add(y);
        list1.addAll(list2);
        list2=null;
        
        printMe(list1);
        removeStuff(list1,2,5);
        printMe(list1);
        reverseMe(list1);
    }
    //printMe method
    private static void printMe(List<String> l){
        for(String b:l)
            System.out.printf("%s",b);
        System.out.println();
    }
    //removestuff method
    private static void removeStuff(List <String> x, int from, int to){
        x.subList(from,to).clear();//builtin methods
    }
    private static void reverseMe(List<String> l){
        ListIterator<String> bobby=l.listIterator(l.size());
        while(bobby.hasPrevious())
            System.out.printf("%s", bobby.hasPrevious());
    }
}

