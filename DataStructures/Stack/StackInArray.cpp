#include<stdio.h>
#include<stdlib.h>
#define MAX_SIZE 101
int A[MAX_SIZE];
int top=-1;
void Push(int x){
	if(top==MAX_SIZE-1){
		printf("Error;stack overflow\n");
	}
	A[++top]=x;
}
void pop(){
	if(top==MAX_SIZE-1){
		printf("Error: No element to pop\n");
	}
	top--;
}
int Top(){
	return A[top];
}
void print(){
	int i;
	printf("Stack :");
	for(i=0;i<=top;i++){
		printf("\n%d",A[i]);
	}
	printf("\n");
}
int main(){
	Push(2);
	print();
	Push(10); 
	print();
	pop();
	Top();
	Push(7);
	print();
	pop();
}

