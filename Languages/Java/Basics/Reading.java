/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
/**
 *
 * @author esoussh
 */
public class Reading {
    public static void main(String[] args) 
    throws IOException{
        BufferedReader br=new BufferedReader(new
        InputStreamReader(System.in));
        System.out.println("Enter an integer:");
        int a= Integer.parseInt(br.readLine());
        System.out.println("Enter a string:");
        String b=br.readLine();
        System.out.printf("You have entered:-"+a+""
                + " and named it as "+b);
    }
}
