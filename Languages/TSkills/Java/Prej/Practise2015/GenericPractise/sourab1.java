package javaapp.intermediate;
import java.util.*;
public class sourab1 {
    public static void main(String args[]){
        String[] crap={"apples","lemons","geese","bacon","youtube"};
        List<String> l1=Arrays.asList(crap);
        Collections.sort(l1);
        System.out.printf("%s \n", l1);
        Collections.sort(l1,Collections.reverseOrder());
        System.out.printf("%s \n", l1);
    }
}
