#include<iostream>
using namespace std;
 
int main()
{
   int x = 10;
   int *ptr = &x;
   int* &ptr1 = ptr;//takes address of *ptr
   cout<<*ptr;
   cout<<endl<<&ptr<<endl;
   cout<<&x;
}
