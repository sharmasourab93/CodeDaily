package Basics;
/*
*   Under standing properties of Static Values in a class
* Another important thing to know about static function is that 
* Static define variables have life throughout the life of the program
* But for usage it is dependent on the scope of the variable
*
*/
public class UsageofStatic {
static int  i=0;
 void ivalue(){
     i=10;
     System.out.println("Value of I in ivalue(): "+i);
 }
 void lvalue(){
     i=20;
     System.out.println("value of I in lvalue(): "+i);
 }
 public static void main(String[] args){
     System.out.println("Value of before calling ivalue(): "+i);
     UsageofStatic u=new UsageofStatic();
     u.ivalue();
     System.out.println("Value of i after calling ivalue(): "+i);
     u.lvalue();
     System.out.println("Value of i after calling lvalue(): "+i);
     i=10;
     System.out.println("Value of i for the one last time: "+i);
 }
}
