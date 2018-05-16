package javaapp;
import java.util.*;
import java.io.*;
import static java.lang.Integer.reverse;
/**
 *
 * @author Sourab Sharma
 */
public class third {
/***
 *
 *
 ***/ 
    //To detect if a string is a palindrome or not
     public static void palindrome(String y){
        int length=y.length();
        String reverse="";
         for ( int i = length - 1; i >= 0; i-- )
         reverse = reverse + y.charAt(i);
         //chartAt() method returns the parameter at the specified parameter
      if (y.equals(reverse))
         System.out.println("Entered string is a palindrome.");
      else
         System.out.println("Entered string is not a palindrome.");
      reverse1(y);
     }
     //Reversal of a string
    public static void reverse1(String s){
        String returnString = "";
        for(int i = s.length()-1; i>=0; i--){
                returnString+=s.charAt(i);
        }
        System.out.println("Reversed string  "+returnString);
        randshuffle(returnString);
    }
    //shuffle it at random
    public static void randshuffle(String x){
        int number=x.length();
        int counter;
        Random r=new Random();
        String y="";
        for(counter=1;counter<=number;counter++){    
            int z=r.nextInt(counter);
            y=y+x.charAt(z);
        }       
        System.out.println("After random shuffle:"+y);
        addchar(y);
    }
    //Using typecasting methods to change the charactersr
    public static void addchar(String x){
        String a = "";
        int counter;
        int teb=x.length();
        for(counter=0;counter<=teb-1;counter++){
            a+=(char)(x.charAt(counter)+1);
        }
        System.out.println("After adding characters continously "+a);
    }
    //main Method
    public static void main(String args[]){
            Scanner scan=new Scanner(System.in);
            System.out.printf("Enter a string to reverse:");
            String x= scan.nextLine();
            palindrome(x);  
    }
}
