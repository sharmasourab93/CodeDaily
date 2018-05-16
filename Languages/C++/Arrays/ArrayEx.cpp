/*Create an array. Fill some elements in it. Delete the first element in the array and push all other elements 
to the front by 1 element*/
#include<iostream>
using namespace std;
int main(){
	int arr[5];
	cout<<"\n Input the number of elements in the array:";
	int i,no;
	cin>>no;
	cout<<"\nInput the numbers";
	for(i=0;i<no;i++){
		cout<<"\n";
		cin>>arr[i];
	}
	int j;
	char x;
	cout<<"\ndo you wish to delete the first number?";
	cin>>x;
	if(x=='y'){
		arr[0]='\0';
	}	
	cout<<arr[0];
	for(j=1;j<=no;j++){
		if(j==no){
			arr[j-1]=arr[no];	
		}else{
			arr[j-1]=arr[j];
		}
	}
	cout<<"\nHey look for the correction:\t";
	for(int k=0;k<no;k++){
		cout<<"\n";
		cout<<arr[k];	
	}
}
