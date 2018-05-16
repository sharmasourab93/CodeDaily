#include<stdio.h>
#define my_sizeof(type) (char *)(&type+1)-(char*)(&type)
int main(){
    int x;
    int c=my_size(x);
    printf("\n%d",c);
    
}
