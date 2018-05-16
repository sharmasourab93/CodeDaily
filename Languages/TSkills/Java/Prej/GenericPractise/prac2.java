package javaapp;
import java.io.*;
import static java.lang.System.exit;
import java.util.Scanner;
public class prac2 {
    public static void main(String args[]){
        String x = null,b = null;
        Scanner scan=new Scanner(System.in);
        x=scan.nextLine();
        b=scan.nextLine();
        if(x==null){
           x=scan.nextLine();
        }else if(b==null){
            b=scan.nextLine();
        }
        System.out.println();
        
        if(b.equals(x)){
            try{
            System.out.println(b+" equals "+x);
        }catch(Exception w){
            System.out.println("Wjta het lehl");
            
        }}else{
            System.out.println("What the hellwa");
        }
        
       
    }
}
