package javaapp.intermediate;
import java.util.*;
public class stacky {
    public static void main(String args[]){
        Stack<String> stack=new Stack<String>();
        stack.push("Neeche");
        printStack(stack);
        stack.push("doosra");
        printStack(stack);
       stack.push("aakhri");
        printStack(stack);
        
        stack.pop();
        printStack(stack);
        stack.pop();
        printStack(stack);
        stack.pop();
        printStack(stack);
    }
    private static void printStack(Stack<String> s){
        if(s.isEmpty()){
            System.out.println("You have nothing in your stack");
        }else{
            System.out.printf("%s TOP\n", s);
        }
    }
}