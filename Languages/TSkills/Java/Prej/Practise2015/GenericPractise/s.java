package javaapp.intermediate;
public class s {
    public static void main(String args[]){
        System.out.println(fact(5));
    }
    //factorial of a number
    public static long fact(long n){
        if (n<=1){
        return 1;
    }else{
            return (n *fact(n-1));
            }
    }
}
