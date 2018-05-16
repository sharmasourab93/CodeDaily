/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
/**
 *
 * @author esoussh
 */
public class ReverseString {
    static String reverse(String string){
        int y=string.length();
        String rev="";
        for(int i=y-1;i>=0;i--){
            rev+=string.charAt(i);
        }
        //System.out.println("The reverse String is :"+rev);
        return rev;
    }
    public static void main(String[] args) throws IOException {
        System.out.print("Please input a string: ");
        String ss=new String();
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        ss=br.readLine();
        System.out.println(ss);
        ReverseString x=new ReverseString();
        System.out.println("\nReversed String: "+reverse(ss));
    }
}
