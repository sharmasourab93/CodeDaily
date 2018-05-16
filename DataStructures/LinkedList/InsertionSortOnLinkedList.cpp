//Insertion Sort on Linked List
#include<iostream>
using namespace std;

struct Node{
	int data;
	Node *next;
};
void sortedInsert(Node **,Node*);

void insertionSort(Node **head){
	Node *sorted=NULL;
	Node *current=*head;
	while(current!=NULL){
		Node *next=current->next;
		sortedInsert(&sorted,current);
		current=next;
	}
	*head=sorted;
}

void sortedInsert(Node **head,Node *newnode){
	Node *current;
	if (*head==NULL || (*head)->data>=newnode->data){
		newnode->next=*head;
		*head=newnode;
	}else{
		current=*head;
		while(current->next!=NULL && current->next->data<newnode->data){
			current=current->next;
		}
		newnode->next=current->next;
		current->next=newnode;
	}
}

void printList(struct Node *head)
{
    struct Node *temp = head;
    while(temp != NULL)
    {
        printf("%d  ", temp->data);
        temp = temp->next;
    }
}

void push(struct Node** head_ref, int new_data)
{
    /* allocate node */
    struct Node* new_node = new Node;
 
    /* put in the data  */
    new_node->data  = new_data;
 
    /* link the old list off the new node */
    new_node->next = (*head_ref);
 
    /* move the head to point to the new node */
    (*head_ref)    = new_node;
}
int main()
{
    struct Node *a = NULL;
    push(&a, 5);
    push(&a, 20);
    push(&a, 4);
    push(&a, 3);
    push(&a, 30);
 
    printf("Linked List before sorting \n");
    printList(a);
 
    insertionSort(&a);
 
    printf("\nLinked List after sorting \n");
    printList(a);
 
    return 0;
}
