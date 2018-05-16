package javaapp;
import static java.lang.System.exit;
import java.util.*;
public class datastruct {
    Scanner s=new Scanner(System.in);
    public int size=5;
    public static int a[]={24,21,43,64,75};
    public int top=size;
    public void mainprogram(){
        System.out.println("Entering Stack Functionality...");
        //System.out.println("\nEnter the no. of rows in the stack:");
        //size=s.nextInt();
        System.out.println("\nWhat do you want to do?");
        System.out.println("\n\t1.Push an Element");
        System.out.println("\n\t2.Pop an Element");
        System.out.println("\n\t3.Peep");
        System.out.println("\n\t4.Stack Structure");//all elements of the stack
        System.out.println("\n\t5.Exit");
        System.out.println("\n Enter your choice:");
        int opt= s.nextInt();
        if(opt>=1||opt<=5){
            option(opt);
        }
    }
    public int option(int a) {
        /***switch(a){
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                peep();
                break;
            case 4:
                struct();
                break;
            default:
                exit(0);    
        }***/
        if(a==1){push();}
        if(a==2){pop();}
        if(a==3){peep();}
        if(a==4){struct();}
        else{exit(0);}
        return 0;
    }

    public void push(){
        if(top==size-1){
            System.out.println("Stack is full, can't push a value");
        }else{
            System.out.println("\nEnter the element you want to enter:");
            top=top+1;
            a[top]=s.nextInt();
            System.out.println(a[top]+" was pushed into the stack.");
        }
    }
    public void pop(){
     if(!isEmpty()){
         System.out.println(a[top]+" popped.");
         a[top]=a[top-1];
         top=top-1;
     }else{
         System.out.println("Cannot be popped.. No element in the stack.");
     }   
    }
     public boolean isEmpty(){
        return top==-1;
    }
    public void peep(){
    
        System.out.println(a[top]+"  is the top most element of the stack.");
    }
    public void struct(){
        for(int i=0;i<=size-1;i++){
            System.out.println(a[i]+" is the "+i+"th element in the stack");
        }
    }
    public static void main(String args[]){
        datastruct g=new datastruct();
        g.mainprogram();
    }
}