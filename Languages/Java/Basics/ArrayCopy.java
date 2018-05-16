package Basics;

import java.util.Arrays;

/**
 *
 * @author esoussh
 */
public class ArrayCopy extends Jan2017{
    public static void main(String[] args){
        Jan2017 n=new Jan2017();
        char[] copyFrom={'d','e','c','a','f','f','e','i','n','a','t','e','d'};
        char[] copyTo=java.util.Arrays.copyOfRange(copyFrom, 2, 9);//new char[7];
        //System.arraycopy(copyFrom, 2, copyTo, 0, 7);
        //Here copyTo var is being typecasted to string
        System.out.println(new String(copyTo));   
        System.out.println(n instanceof Jan2017);
        int arr1[]={10,20,30};
        int arr2[]={10,20,30};
        if(arr1==arr2){
            System.out.println("Same");
        }else{
            System.out.println("not same");
        }
        if(Arrays.equals(arr1,arr2)){
            System.out.println("Same");
        }else{
            System.out.println("not same");
        }
        //Arrays.deepEquals returns the arrs wrapped inside an object
   
    }
}
