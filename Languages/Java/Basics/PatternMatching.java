/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
/**
 *
 * @author esoussh
 */
public class PatternMatching {
    public static void main(String[] args){
        Pattern pattern=Pattern.compile("Geeksf",Pattern.CASE_INSENSITIVE);
        Matcher m=pattern.matcher("geeksforgeeks");
        while(m.find()){
            System.out.println("Pattern found between "+m.start()+"to "+m.end());
        }
    }
}
