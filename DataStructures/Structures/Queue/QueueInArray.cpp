/*Array based Priority Queuing*/ 
#include<iostream>
#include<stdlib.h>
using namespace std;
class Q{
	public:
		struct ArrQ{
			int data;
			int priority;
		};
		ArrQ x[7],temp;
		void enqueue(){
			int i=0;
			while(i<7){
				if(i==0){
					cout<<"First PQueue: ";
					cout<<"Enter first data: ";
					cin>>x[i].data;
					cout<<"Priority: ";
					cin>>x[i].priority;
				}
				else{
					cout<<"Data "<<i+1<<"th place: ";
					cin>>x[i].data;
					cout<<"Priority: ";
					cin>>x[i].priority;	
				}
			i++;
			}
			printQ();
			prioritize();
		}
		void prioritize(){
			for(int j=0;j<7;j++){
				for(int k=j+1;k<7;k++){
					if(x[j].priority>x[k].priority){
						temp=x[j];	
						x[j]=x[k];
						x[k]=temp;
					}else{
						continue;
					}	
				}
			}
			printQ();
		}
		void dequeue(){
			int l;
			x[0].data='\0';
			x[0].priority='\0';
			for(l=0;l<7;l++){
				x[l]=x[l+1];
			}
			cout<<"Dequeued!"<<endl;
			printQ();
		}
		void printQ(){
			cout<<"\nPrinting Queue!"<<endl;
			int size=sizeof(x)/sizeof(x[0]);
			cout<<"\nData\tPriority"<<endl;
			for(int a=0;a<size;a++){
				cout<<x[a].data<<"\t"<<x[a].priority<<endl;
			}
		}
		void execute(){
			enqueue();
			dequeue();
			dequeue();
		}
};
int main(){
	Q q;
	q.execute();
}
