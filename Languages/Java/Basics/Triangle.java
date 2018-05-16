/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;
import java.io.*;
/**
 *
 * @author esoussh
 */
public class Triangle {
    public static void printTriangle(int n){
        int k=(2*n)-2;
        for(int i=0;i<n;i++){
            for(int j=0;j<=k;j++){
                System.out.print(" ");
            }
            k=k-1;
            for(int j=0;j<=i;j++){
                System.out.print("*");
            }
            System.out.println("");
            
        }
    }
    public static void main(String[] args) {
        int n=5;
        printTriangle(5);
    }
}
