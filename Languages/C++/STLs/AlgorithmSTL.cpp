#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
void show(int a[]){
	for(int i=0;i<10;i++){
		cout<<" "<<a[i];
	}
}
int main(){
	int a[10]={1,5,8,9,7,3,4,2,0,6};
	cout<<" The array before sorting is: "<<endl;
	show(a);
	sort(a,a+10);
	cout<<"\n THe array after sorting is: "<<endl;
	show(a);
	if(binary_search(a,a+10,3)){
		cout<<"\nElement found! "<<lower_bound(a,a+10,3)-a<<endl;
	}else{
		cout<<"\nNot found!"<<endl;
	}
	reverse(a,a+10);
	show(a);
	return 0;
}
