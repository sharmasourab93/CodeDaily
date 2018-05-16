//Program for First Come First Serve Scheduling 
#include<iostream>
using namespace std;
void findWaitingTime(int processes[],int n,int bt[],int wt[]){
	wt[0]=0;
	for(int i=1;i<n;i++){
		wt[i]=bt[i-1]+wt[i-1];
	}
}
void findTurnAroundTime(int processes[],int n,int bt[],int wt[],int tat[]){
	for(int i=0;i<n;i++){
		tat[i]=bt[i]+wt[i];
	}
}
void findavgTime(int processes[],int n,int bt[]){
	
	int wt[n],tat[n],total_wt=0,total_tat=0;
	findWaitingTime(processes,n,bt,wt);
	findTurnAroundTime(processes,n,bt,wt,tat);
	
	cout<<"Processes "<<" Burst time  "<<" Waiting Time "<<" Turn Around Time \n";
	for(int i=0;i<n;i++){
		total_wt=total_wt+wt[i];
		total_tat=total_tat+tat[i];
		cout<<"  "<<i+1<<"\t\t"<<bt[i]<<"\t   "<<wt[i]<<"\t\t  "<<tat[i]<<endl;
	}
	cout<<"Average waiting time= "<<(float)total_wt/(float)n<<endl;
	cout<<"Average Turn around time= "<<(float)total_tat/(float)n<<endl;
}
int main(){
	//Process IDs
	int processes[]={1,2,3};
	int n=sizeof(processes)/sizeof(processes[0]);
	//Burst Time of all processes
	int burst_time[]={10,5,8};
	
	findavgTime(processes,n,burst_time);
}
