/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Generics;

/**
 *
 * @author esoussh
 */
public class GenericMethodTest {
  //generic method printArray
    public static <E> void printArray(E[] inputArray){
        //Display array elements
        for(E element: inputArray){
            System.out.printf("%s\t",element);
        }
        System.out.println();
    }
    public static void main(String[] args) {
        //Create arrays of Integer, double & Character
        Integer[] intArray={1,2,3,4,5};
        Double[] doubleArray={1.1,2.2,3.3,4.4,5.5};
        Character[] charArray={'H','E','L','L','O'};
        System.out.println("Array integerArray");
        printArray(intArray);
        System.out.println();
        printArray(doubleArray);
        System.out.println();
        printArray(charArray);
    }
}
