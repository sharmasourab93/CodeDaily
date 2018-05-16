//Threads Program 
#include<iostream>
#include<pthread>
using namespace std;
#define NUM_T 5
void *PrintHello(long *threadid){
	long *tid;
	tid=threadid;
	cout<<"Hello WOrld! Thread id"<<tid<<endl;
	pthread_exit(NULL);
}
int main(){
	pthread_t threads[NUM_T];
	int rc;
	int i;
	for(i=0;i<NUM_T;i++){
		cout<<"main(): creating thread, "<<i<<endl;
		rc=pthread_create(&threads[i],NULL,PrintHello,i);
		if(rc){
			cout<<"Error: unable to create thread,"<<rc<<endl;
			exit(-1);
		}
	}
	pthread_exit(NULL);
}
