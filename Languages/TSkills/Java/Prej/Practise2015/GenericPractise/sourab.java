package javaapp.intermediate;
import java.util.*;
public class sourab {
    public static void main(String args[]){
        String[] stuff={"babies","water melon","fudge","melongs"};
        LinkedList<String> thelist=new LinkedList<String>(Arrays.asList(stuff));
        //simply appended
        thelist.add("pumpkins");
        //added at the beginning
        thelist.addFirst("firstthing");
        //convert back to an array
        stuff=thelist.toArray(new String[thelist.size()]);
        
        for(String x: stuff)
               System.out.printf(" %s ", x);
        
    }
}
