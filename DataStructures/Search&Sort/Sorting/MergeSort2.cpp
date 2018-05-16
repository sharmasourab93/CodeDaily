//Merge Sort 
#include<iostream>
using namespace std;
class MergerSort{
	public:
		void merge(int array[],int low, int mid, int rear){
			int i,j,k;
			int n1=(mid-low+1);
			int n2=(rear-mid);
			int L[n1], R[n2];
			for(i=0;i<n1;i++) L[i]=array[low+i];
			for(j=0;j<n2;j++) R[j]=array[mid+1+j];
			i=0;
			j=0;
			k=low;
			while(i<n1 && j<n2){
				if(L[i]<=R[j]){
					array[k]=L[i];
					i++;
				}else{
					array[k]=R[j];
					j++;
				}
			}
			while(i<n1){
				array[k]=L[i];
				i++;
				k++;
			}
			while(j<n2){
				array[k]=R[j];
				k++;
				j++;
			}
		}
		int midindex(int a, int b){
			return ((a+(b-a)/2));
		}
		void mergesort(int array[],int low, int rear){
			static int i;
			cout<<"Entering Merge Sort "<<++i<<endl;
			if(low<rear){
				int m=midindex(low,rear);
				mergesort(array,low,m);
				mergesort(array,m+1,rear);
				merge(array,low,m,rear);
			}
		}
		int func(){
			int array[]={6,32,45,12,78,84,99};
			int l=0;
			int r=((sizeof(array))/(sizeof(array[0])));
			cout<<"Merge Sort Function Begins"<<endl;
			mergesort(array,l,r);
		}
};
int main(){
	MergerSort ms;
	ms.func();
}
