package datastructures;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import static java.lang.System.exit;
import java.util.*;
public class llist1 {
    List<String> list1=new LinkedList<String>();
    BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
    Scanner scan=new Scanner(System.in);
    static void choiceopt(){
            System.out.println("\n Welcome to the class linked list");
            System.out.println("\n Options to Choose:");
            System.out.println("\n1.Insert an Element at beginning");
            System.out.println("\n2.Insert an Element at the ith position");
            System.out.println("\n3.Insert an Element at the end");
            System.out.println("\n4.Delete an element at the front");
            System.out.println("\n5.Delete an element at the ith position");
            System.out.println("\n6.Delete an element at the end");
            System.out.println("\n7.Print the Linked list");
            System.out.println("\n8.Exit");
            System.out.println("\nEnter your choice:");
            static int choice=scan.nextInt();
            switch (choice){
                    case 1:
                    insertbegin();
                    break;
                    case 2: 
                    insertati();
                    break;
                    case 3: 
                    insertatend();
                    break;
                    case 4: 
                    deleteatbegin();
                    break;
                    case 5: 
                    deleteati();
                    break;
                    case 6: 
                    deleteatend();
                    break;
                    case 7:
                    printlist();
                    break;
                    case 8:
                    exit('\0');
            }		
    }
    public static void main(String[] args){
        int x=1;
        while(x!=0){
        choiceopt();
    }
            
    }

    private static void insertbegin(){
        static List<String> temp=new LinkedList<String>();
        temp=list1;

        
    }

    private static void insertati() {
        
    }

    private static void insertatend() {
        
    }

    private static void deleteatbegin() {
        
    }

    private static void deleteati() {
        
    }

    private static void deleteatend() {
        
    }

    private static void printlist() {
        
    }
}
