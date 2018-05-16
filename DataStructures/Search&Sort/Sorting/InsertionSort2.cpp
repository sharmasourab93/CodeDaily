//Insertion Sort Algorithm 
#include<iostream>
using namespace std;
class InsertionSort{
public:
	void swap(int a, int b)
	{	
		int t=a;
		a=b;
		b=t;
	}
	void IsSort(){
		int size;
		int x[size];
		cout<<"\nEnter the desired size of the array";
		cin>>size;
		//Inputting the size & getting the sorted set of array
		for(int i=0;i<size;i++){
			cin>>x[i];
		}
		for(int j=2;j<size;j++){
			for(int k=j;k>1;k--){
				while(x[k]<x[k-1]){
					swap(x[k],x[k-1]);
				}
			}
		}
		cout<<"The Elements after sorting are: "<<endl;
		for(int a=0;a<size;a++){
			cout<<x[a]<<endl;
		}
	}
};
int main(){
		InsertionSort is;
		cout<<"Welcome to Insertion Sort Algorithm: ";
		is.IsSort();
		return(0);
	}	
 
