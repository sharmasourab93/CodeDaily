/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Collection;
import java.util.*;
import java.io.*;
//import java.util.Iterator;
/**
 *
 * @author esoussh
 */
public class Iterators1 {
    public static void main(String[] args){
        int arr[]=new int[]{1,2,3,4};
        Vector<Integer> v=new Vector();
        Hashtable<Integer,String>h=new Hashtable();
        v.addElement(1);
        v.addElement(2);
        h.put(1,"geeks");
        h.put(2,"4 geeks");
        h.put(7,"Selfie lele");
        //Array instance creation requires[], while Vector
        //and hastable require()
        //Vector element insertion requires addElement(), but
        //Hashtable element insertion requires put()
        
        //Accessing first element of array, vector and hashtable 
        System.out.println(arr[0]);
        System.out.println(v.elementAt(0));
        //Iterator iter=h.iterator();
        
        
        //Array elements are accessed using[], vector elements 
        //using elementAt() and hashtable elements using get()
    }
}
