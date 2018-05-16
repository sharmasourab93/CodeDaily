//Max Heap 
#include<iostream>
#include<climits>
using namespace std;
class MaxHeap{
	int *harr;
	int heap_size;
	int capacity;
	public:
		MaxHeap(int cap){
			//int *harr;
			harr=new int[cap];
			heap_size=0;
			capacity=cap;
		}
		int parent(int i){
			return (i-1)/2;
		}
		int left(int i){
			return (2*i+1);
		}
		int right(int i){
			return (2*i+2);
		}
		int getMax(){
			return harr[0];
		}
		void swap(int *a, int *b){
			int temp=*a;
			*a=*b;
			*b=temp;
		}
		void insertKey(int key){
			if(heap_size==capacity){
				cout<<"\nOver flow condition"<<endl;
				return;
			}
			heap_size++;
			int index=heap_size-1;
			harr[index]=key;
			while( index!=0 && harr[parent(index)]<harr[index] ){
				swap(&harr[parent(index)],&harr[index]);
				index=parent(index);
			}
		}
		void decreaseKey(int i, int new_val){
			harr[i]=new_val;
			while( i!=0 && harr[parent(i)]<harr[i]){
				swap(&harr[parent(i)],&harr[i]);
				i=parent(i);
			}
		}
		void maxheapify(int i){
			int l=left(i);
			int r=right(i);
			int largest=i;
			if(l<heap_size && harr[i]>harr[l]){
				largest=l;
			}
			if(r<heap_size && harr[largest]>harr[r]){
				largest=r;
			}
			if(largest!=i){
				swap(&harr[i],&harr[largest]);
				maxheapify(largest);
			}
		}
		int extractmax(){
			if(heap_size<=0){
				return INT_MAX;
			}
			if(heap_size==1){
				heap_size--;
				return harr[0];
			}
			int root=harr[0];
			harr[0]=harr[heap_size-1];
			heap_size--;
			maxheapify(0);
			return root;
		}
		void deleteKey(int i){
			decreaseKey(i,INT_MAX);
			extractmax();
		}
		void printArray(){
			cout<<"\nPrinting elements in the array which is heaped:"<<endl;
			for(int i=0;i<capacity;i++){
				cout<<harr[i]<<" ";
			}
			cout<<endl;
		}
		
};
int main(){
	int arr[]={10,9,4,6,1,11,12};
	int size=(sizeof(arr)/sizeof(arr[0]));
	int i=0;
	MaxHeap mx(size);
	mx.insertKey(arr[i]);i++;
	mx.insertKey(arr[i]);i++;
	mx.insertKey(arr[i]);i++;
	mx.deleteKey(i);
	mx.insertKey(arr[i]);i++;
	mx.insertKey(arr[i]);i++;
	mx.insertKey(arr[i]);i++;
	cout<<"\nExtracting max element: "<<mx.extractmax()<<endl;
	cout<<"\Getting max element: "<<mx.getMax()<<endl;
	cout<<"\nPrinting all the elements in the array: "<<endl;
	mx.printArray();
}
