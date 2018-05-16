/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ENUM;
// A Simple enum example where enum is declared 
//outside any class 
/*
    All enums are implicitly public static final
    Since it is final, it cannot have children classes
*/
//  Main method can be declared inside an enum
enum Color{
    Red,Green, Blue;
}
/**
 *
 * @author esoussh
 */
public class FirstEnum {
    //Driver Method
    public static void main(String[] args) {
        Color c1= Color.Red;
        Color arr[]=Color.values();
        System.out.println(c1);
        for(Color or:arr){
            int usingord=or.ordinal()+1;
            System.out.println(or+" at index "+usingord);
        }
    }
}
