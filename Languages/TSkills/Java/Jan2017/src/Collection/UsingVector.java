/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Collection;
import java.util.*;
/**
 *
 * @author esoussh
 */
public class UsingVector {
    public static void main(String[] args){
        Vector<String> daynames=new Vector<>();
        daynames.add("Sunday");
        daynames.add("Monday");
        daynames.add("Tueday");
        daynames.add("Wedday");
        daynames.add("Thursday");
        daynames.add("Friday");
        daynames.add("Satday");
        Enumeration days=daynames.elements();
        while(days.hasMoreElements()){
            System.out.println(days.nextElement());
        }
    }
}
