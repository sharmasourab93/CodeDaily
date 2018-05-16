//Max Heap Self
#include<iostream>
#include<climits>
using namespace std;
void swap(int *a,int *b){
	int temp=*a;
	*a=*b;
	*b=temp;
}
class Heap{
	int *array;
	int capacity;
	int heap_size;
	public:
		Heap(int cap){
			heap_size=0;
			capacity=cap;
			array=new int[cap];
		}
		int parent(int i){return ((i-1)/2);}
		int left(int i){return ((2*i)+1);}
		int right(int i){return((2*i)+2);}
		int getmax(){return array[0];}
		int MaxHeapify(int i){
			int l=left(i);
			int r=right(i);
			int largest=i;
			if(l>heap_size && array[l]>array[i]){largest=l;}
			if(r>heap_size && array[r]>array[largest]){largest=r;}
			if(largest!=i){
				swap(&array[i],&array[largest]);
				MaxHeapify(largest);
			}
		}
		int extractMax(){
			if(heap_size<=0){return INT_MAX;}
			if(heap_size==1){heap_size--;return array[0];}
			int root=array[0];
			array[0]=array[heap_size-1];
			heap_size--;
			MaxHeapify(0);
			return root;
		}
		void insertkey(int value){
			if(heap_size!=capacity)
				heap_size++;
				int i=heap_size-1;
				array[i]=value;
				while(i!=0 && array[parent(i)]>array[i]){
					swap(&array[i],&array[parent(i)]);
					i=parent(i);
				}	
		}
		void deletekey(int i){
			decreasekey(i,INT_MIN);
			extractMax();
		}
		void decreasekey(int i,int new_val){
			array[i]=new_val;
			while(i!=0 && array[parent(i)]<array[i]){
				swap(&array[i],&array[parent(i)]);
				i=parent(i);
			}
		}
};
int main(){
	Heap h(7);
	h.insertkey(10);
	h.deletekey(10);
	h.insertkey(15);
	h.deletekey(15);
	h.insertkey(12);
	h.insertkey(87);
	h.insertkey(45);
	h.insertkey(25);
	h.insertkey(35);
	cout<<h.getmax()<<endl;
	h.deletekey(87);
	cout<<h.extractMax()<<endl;
}
