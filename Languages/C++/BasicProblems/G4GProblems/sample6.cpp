#include<iostream>
using namespace std;
 
int &fun()
{
    int x = 10;//if static accepts the new value changes else doesn't
    return x;
}
int main()
{
    fun() = 30;
    cout << fun();
    return 0;
}
