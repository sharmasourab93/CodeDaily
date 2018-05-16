#include<iostream>
//I/P =[1,2,3,2,3,1,3]
//O/P=3
/*
*Given an array of positive integers.
*All numbers occur even number of times except one number
*which occurs odd number of times.
*Find the number in O(n) time & constant space.
*/
using namespace std;
int main(){
	struct Max{
		int element;
		int count;
	};
	Max head[6];
	int array[]={7,2,3,7,3,1,4};
	int i=1,j;
	head[0].element=array[0];
	head[0].count=1;
	while(i<7){
		//for(int j=i-1;j>=0;j--){
		j=i-1;
		while(j>=0){
			if(head[j].element==array[i]){
				head[j].count++;
			}else if(head[j].element!=array[i]){
				head[i].element=array[i];
				head[i].count=1;
			}
			j--;
		}
		i++;
	}
	for(int k=0;k<7;k++){
		cout<<head[k].element<<" "<<head[k].count<<endl;
	}
}

