//Find if an element is an ascending, descending, ascending descending or 
//descending ascending 
#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
void findArray(int *array,int size){
		int i=0;
		if(array[i]<array[i+1]){
			cout<<"Ascending"<<endl;
		}else{
			cout<<"\nDescending"<<endl;
		}
		if(array[size-1]<array[size-2]){
			cout<<"\nDescending"<<endl;
		}else{
			cout<<"Ascending"<<endl;
		}
}
void findAbsoluteOrder(int *array,int size){
	srand(time(0));
	cout<<"Time(0) "<<time(0)<<endl;
	int RandIndex1=rand()%(size/2);
	int RandIndex2=rand()%(size);
	cout<<"Random1 "<<RandIndex1<<" "<<"Random2 "<<RandIndex2<<endl;
		if(array[RandIndex1]<array[RandIndex2]){
			cout<<"Ascending";
		}else if(RandIndex1==RandIndex2){
			if(array[RandIndex1]<array[RandIndex2+1]){
				cout<<"Ascending";
			}else{
				cout<<"Descending";
			}
		}else{
			cout<<"Descending";
		}
}
int main(){
	int array[]={4,3,2,1,10,11,12,13};
	int arr[]={7,6,5,4,3,2,1};
	int size1=((sizeof(arr))/(sizeof(arr[0])));
	int size=((sizeof(array))/(sizeof(array[0])));
	findArray(array,size);
	findAbsoluteOrder(arr,size1);
	
}
