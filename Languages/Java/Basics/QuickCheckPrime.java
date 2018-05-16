/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.util.*;
import java.math.*;
/**
 *
 * @author esoussh
 */
public class QuickCheckPrime {
    static boolean checkPrime(long n){
        BigInteger b=new BigInteger(String.valueOf(n));
        return b.isProbablePrime(1);
    }
    static long nextPrime(long n){
        BigInteger b=new BigInteger(String.valueOf(n));
        return Long.parseLong(b.nextProbablePrime().toString());
    }
    public static void main(String[] args)
            throws java.lang.Exception  {
        long n=16;
        System.out.println(checkPrime(n));
        System.out.println(nextPrime(n));
    }
}
