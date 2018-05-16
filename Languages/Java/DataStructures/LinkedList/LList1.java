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
//Alternate way to build a linkedList
public class LList1 {
    Node head;
    static class Node{
        int data;
        Node next;
        Node(int d){data=d;next=null;}
    }
    public static void main(String[] args) throws NullPointerException{
        LList1 llist =new LList1();
        llist.head=new Node(1);
        Node Second=new Node(2);
        Node third=new Node(3);
        llist.head.next=Second;
        Second.next=third;
        third.next=null;
        Node tnode=llist.head;
        while(tnode!=null){
            System.out.println(tnode.data);
            tnode=tnode.next;
        }
        
    }
}
