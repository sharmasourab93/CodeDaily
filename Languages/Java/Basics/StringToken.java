/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.util.StringTokenizer;
/**
 *
 * @author esoussh
 */
public class StringToken {
    public static void main(String[] args) {
        StringTokenizer st1;
        st1 = new StringTokenizer("Hello Sourab Sharma How are you?"," ");
        while(st1.hasMoreTokens()){
            System.out.println(st1.nextToken());
        }
    }
}
