#include <stdio.h>
int main()
{
   void *vptr;
   int *iptr = vptr;
   //In C++, it must be replaced with int *iptr=(int *)vptr; 
   return 0;
}