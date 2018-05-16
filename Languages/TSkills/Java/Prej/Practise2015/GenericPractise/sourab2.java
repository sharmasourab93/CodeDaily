package javaapp.intermediate;
import java.util.*;
public class sourab2 {
    public static void main(String args[]){
        //create an array and convert to list
        Character[] ray={'p','w','n'};
        List<Character> l= Arrays.asList(ray);
        System.out.println("List is :");
        output(l);
        
        //reverse and print the list
        Collections.reverse(l);
        System.out.println("After reverse:");
        output(l);
        
        //create new array and a new list
        Character[] newRay=new Character[3];
        List<Character> listCopy=Arrays.asList(newRay);
        
        //copy the contents of the list
        Collections.copy(listCopy, l);
        System.out.println("Copy of list:");
        output(listCopy);
        //fill collection with crap
        Collections.fill(l,'X');
        System.out.println("After filling the list:");
        output(l);
    }
    //output method
    private static void output(List<Character> thelist){
        for(Character thing: thelist){
            System.out.printf(" %s ",thing);
            System.out.println();
        }
    }
}
