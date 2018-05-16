//Cycle Detection Using Union Find Method
//Referred from GeeksforGeeks for better understanding
#include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;
//A structure to represent an Edge in a graph
struct Edge{
	int src,dest;
};
//A structure to represent Graph
struct Graph{
	int V,E;
	struct Edge* edge;
};
//Creates a graph with V Vertices and E edges
struct Graph* createGraph(int V, int E){
	struct Graph* graph=(Graph*)malloc(sizeof(Graph));
	graph->V=V;
	graph->E=E;
	graph->edge=(Edge*)malloc(sizeof(Edge));
	return graph;
}
//A utility function to find the subset of an element i
int find(int parent[],int i){
	if(parent[i]==-1) return i;
	return find(parent,parent[i]);
}
//A utilityy function to do union of two subsets
void Union(int parent[],int x,int y){
	int xset=find(parent,x);
	int yset=find(parent,y);
	parent[xset]=yset;
}
//Main function to check whether a given graph contains cycle or not
int isCycle(Graph* graph){
	//Allocate memory for creating V subsets
	int *parent=(int*)malloc(graph->V *sizeof(int));
	//Initialize all subsets as single element sets
	memset(parent,-1,sizeof(int)*graph->V);
	
	//Iterate through all edges of graph, find subset of both
	//Vertices of every edge, if both subsets are same, then
	//there is cycle in graph.
	for(int i=0;i<graph->E;++i){
		int x=find(parent,graph->edge[i].src);
		int y=find(parent,graph->edge[i].dest);
		
		if(x==y){return 1;}
		Union(parent,x,y);
	}
	return 0;
}
//Driver program to test above function
int main(){
	int V=3,E=3;
	Graph* graph=createGraph(V,E);
	//add edge 0-1
	graph->edge[0].src=0;
	graph->edge[1].dest=1;
	
	//add edge 1-2
	graph->edge[1].src=1;
	graph->edge[1].dest=2;
	//add edge 0-2
	graph->edge[2].src=0;
	graph->edge[2].dest=2;
	
	if(isCycle(graph))
	{
		cout<<"Graph Contains Cycle";	
	 } 
	else{
		cout<<"Graph doesn't contain cycle";	
	} 
	return 0;
}
