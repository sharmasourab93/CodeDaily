//Finding Second smallest array 
#include<iostream>
using namespace std;
void findSecondSmallest(int *array,int size){
	int f=10000;
	int s=10000;
	for(int i=0;i<size;i++){
		if(array[i]<f){
			s=f;
			f=array[i];
			
		}
		else if(array[i]<s && array[i]!=f){
			s=array[i];
		}
	}
	cout<<s;
}
int main(){
	int array[]={10,20,9,5,45,60};
	int size=sizeof(array)/sizeof(array[0]);
	findSecondSmallest(array,size);
	
}
