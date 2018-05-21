/*Code for Merge Sort Algorithm*/
#include<iostream>
#include<math.h>
using namespace std;
class MergeSort{
	public:
		//Recursive Function which splits and sorts
		void mergersort(int arr[],int findex,int rindex){
			int midindex;
			cout<<"Entering MergerSort"<<"\t";
			if(findex<rindex){
				//cout<<" Entering Loop in it"<<endl;
				midindex=((findex+rindex)/2);
				mergersort(arr,findex,midindex);
				mergersort(arr,midindex+1,rindex);
				merge(arr,findex,midindex,rindex);
			}
		}
		
		//Function to Merge
		void merge(int a[],int f,int m,int r){
			//cout<<"\nEntering Merge Function"<<endl;
			int size=(sizeof(a)/sizeof(a[0]));
			int b[size];
			int i,j,k=0;
			i=f;
			j=m+1;
			while(i<=m&&j<=r){
				if(a[i]<a[j]){
					b[k++]=a[i++];
				}else{
					b[k++]=a[j++];
				}
			}
			while(i<=m){
				b[k++]=a[i++];
			}
			while(j<=r){
				b[k++]=a[j++];
			}
			for(int i=r;i>=0;i--){
				a[i]=b[--k];
			}
		}
		void exec(){
			int array[]={9,6,2,1,7,8,5};
			int first=0;
			int rear=( ( sizeof(array) )  /  sizeof( array[0] ) );
			mergersort(array,first,rear);
		}
		
};
int main(){
	MergeSort ms;
	ms.exec();
}
