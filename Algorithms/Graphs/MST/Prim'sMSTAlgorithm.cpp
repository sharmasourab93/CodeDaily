//Prim's Minimum spanning tree for matrix representation 
//referred from Geeks for geeks
#include<iostream>
#include<climits>
//Number of vertices in the graph
#define V 5
using namespace std;
//A Utility function to find the vertex with minimum key value, from 
// the set of vertices not yet included in MST
int minKey(int key[], bool mstSet[]){
	int min =INT_MAX, min_index;
	for(int v=0;v<V;v++){
		if(mstSet[v]==false && key[v]<min)
			min=key[v],min_index=v;
	}
	return min_index;
}
// A utility function to print the constructed MST stored in parent[]
int printMST(int parent[],int n, int graph[V][V]){
	cout<<"Edge weight\n";
	for(int i=1;i<V;i++){
		cout<<parent[i]<<"-"<<i<<" "<<graph[i][parent[i]]<<endl;
	}
}
//Function to construct and print MST for a graph represented using adjancency matrix representation 
void primMST(int graph[V][V]){
	//Array to store consturcted MST
	int parent[V];
	//Key values used to pick minimum weight edge in cut
	int key[V];
	//To represent set of vertices not yet included in MST
	bool mstSet[V];
	//Initialize all keys as INFINITE
	for(int i=0;i<V;i++){
		key[i]=INT_MAX, mstSet[i]=false;
	}
	//Always include first vertex in MST
	key[0]=0;
	//First node is always root of MST
	parent[0]=-1;
	//THe MST will have V vertices
	for(int count=0;count<V-1;count++){
		//Pick the minimum key vertex from the set of vertices not yet included in MST
		int u=minKey(key, mstSet);
		//Add the picked vertex to the MST set
		mstSet[u]=true;

		//Update key value and paent index of the adjancent vertices of the picked vertex
		//Consider only those vertices which are not yet included in MST
		for(int v=0;v<V;v++){
			//graph[][] is non zero only for adjancent vertices of m
			//mstset[v] is false for vertices not yet included in MST
			//update the key only if graph[u][v] is smaller than key[v]
			if(graph[u][v] && mstSet[v]==false && graph[u][v]<key[v]){
				parent[v]=u, key[v]=graph[u][v];
			}
		}
	}
	//Print the constructed MST
	printMST(parent, V, graph);
}
//Driver program to test above function 
int main(){
	int graph[V][V]={
		{0,2,0,6,0},{2,0,3,8,5},
		{0,3,0,0,7},{6,8,0,0,9},
		{0,5,7,9,0},
	};
	primMST(graph);
	return 0;
}
