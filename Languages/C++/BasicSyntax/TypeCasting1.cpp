//Typecasting and setting precision
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
int a=10;
int b=20;
float f=30.25;
float z=(float)(f/b);
cout<<setprecision(3)<<z;
}
