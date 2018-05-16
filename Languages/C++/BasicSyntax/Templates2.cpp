//Templates 2
#include<iostream>
template <typename T>
void swap(T &n1, T &n2){
	T temp;
	temp=n1;
	n1=n2;
	n2=temp;
}
int main(){
	int i1=1;
	int i2=2;
	swap(i1,i2);
	std::cout<<i1 <<" "<<i2;
}
