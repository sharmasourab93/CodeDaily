#include<iostream>
using namespace std;

template <typename T>
T const& Max(T const& a, T const& b){
	return a<b ? b:a;
}
int main
