/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.util.Random;
/**
 *
 * @author esoussh
 */
public class GenerateRandom {
    public static void main(String[] args) {
        Random rand=new Random();
        int rand_int1=rand.nextInt(4);
        int rand_int2=rand.nextInt(1000);
        
        //print random integers
        System.out.println("Random Integers "+rand_int1);
        System.out.println("Rnadom Integers "+rand_int2);;
        
    }
}
