#include<iostream>
using namespace std;
int main(){
	struct Max{
		int element;
		int count;
	};
	Max *head;
	int array[]={7,3,2,4,7,1,3};
	head=new Max[1];
	head[0].element=array[0];
	head[0].count=1;
	int i=1,j,k;
	for(i,k=0;i<7;i++){
		j=i-1;
		while(j>=0){
			if(head[j].element==array[i]){
				head[j].count++;
			}else{
				head=new Max[++k];
				head[k].element=array[k];
				head[k].count=1;
			}
			j--;
		}
	}
	for(int k=0;k<5;k++){
		cout<<head[k].element<<" "<<head[k].count<<endl;
	}
}
