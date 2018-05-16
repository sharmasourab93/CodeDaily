/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DataStructures.LinkedList;
/**
 *
 * @author esoussh
 */
public class DetectnRemoveLoops {
    static Node head;
    static class Node{
        int data;
        Node next;
        Node(int d){
            data=d;
            next=null;
        }
    }
    int detectAndRemoveLoop(Node node){
        Node slow=node,fast=node;
        while(slow!=null && fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
            //if slow and fast meet at the same point then
            //the loop exists
            if(slow==fast){
                removeLoop(slow,node);
                return 1;
            }
        }
        return 0;
    }
    void removeLoop(Node loop,Node head){
        Node ptr1=loop;
        Node ptr2=loop;
        int k=1,i;
        while(ptr1.next!=ptr2){
            ptr1=ptr1.next;
            k++;
        }
        ptr1=head;
        ptr2=head;
        for(i=0;i<k;i++){
            ptr2=ptr2.next;
        }
        while(ptr2!=ptr1){
            ptr1=ptr1.next;
            ptr2=ptr2.next;
        }
        ptr2=ptr2.next;
        while(ptr2.next!=ptr1){
            ptr2=ptr2.next;
        }
        ptr2.next=null;
    }
    void printlist(Node node){
        while(node!=null){
            System.out.println(node.data+" ");
            node=node.next;
        }
    }
    public static void main(String[] args) {
        DetectnRemoveLoops list=new DetectnRemoveLoops();
        list.head=new Node(50);
        list.head.next=new Node(20);
        list.head.next.next=new Node(15);
        list.head.next.next.next=new Node(4);
        list.head.next.next.next.next=new Node(10);
        
        //Creatng a loop for testing
        head.next.next.next.next.next=head.next.next;
        list.detectAndRemoveLoop(head);
        System.out.println("Linked Lisst after removing loop:");
        list.printlist(head);
    }
}
