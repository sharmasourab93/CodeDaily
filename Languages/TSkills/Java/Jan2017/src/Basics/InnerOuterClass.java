package Basics;
public class InnerOuterClass {
    int x=10;
    public static void main(String[] args){
       InnerOuterClass c=new InnerOuterClass();
       c.m();
       System.out.println("Terminates Here");
    }
    class InnerClass{
        InnerClass(){
            System.out.println("Printing in Inner Class"+x);
        }
        void InnerMain(){
            System.out.println("Inner Class main function");
        }
    }
    void m(){
        System.out.println("Function of the InnerOuterClass m()");
        InnerClass v=new InnerClass();
        v.InnerMain();
    }
}
