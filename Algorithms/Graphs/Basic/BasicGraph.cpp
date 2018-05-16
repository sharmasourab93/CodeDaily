//Graph and its representation
//Geeks4Geeks source Code
#include<iostream>
#include<stdlib.h>
using namespace std;
//A structure to represent an adjacency list node
struct AdjListNode{
	int dest;
	AdjListNode* next;
};
//A structure to represent an adjacency list 
struct AdjList{
	 //pointer to head node of list
	AdjListNode *head;
};
// A structure to represent a graph. A graph is an array of adjacency lists.
//Size of array will be V (number of vertices in graph)
struct Graph{
	int V;
	AdjList* array;
};
//A Utility function to create a new adjacency list node
struct AdjListNode* newAdjListNode(int dest){
	AdjListNode* newNode=new AdjListNode();
	newNode->dest=dest;
	newNode->next=NULL;
	return newNode;
}
// A utility function that creates a graph of V vertices
struct Graph* createGraph(int V){
	Graph* graph=new Graph();
	graph->V=V;
	//Create an array of adjacency lists. Size of array will be V
	graph->array=(AdjList*)malloc(V* sizeof(AdjList));
		//Initialize each adjacency list as empty by making head as NULL
		int i;
		for(i=0;i<V;++i){
			graph->array[i].head=NULL;
		}
		return graph;
}
//Adds an edge to an undirected graph
void addEdge(Graph* graph, int src, int dest){
	//Add an edge from src to dest. A new node is added to the adjacency
	//list of src. The node is added at the begining
	AdjListNode* newNode=newAdjListNode(dest);
	newNode->next=graph->array[src].head;
	graph->array[src].head=newNode;
	
	//since Graph is undirected, add an edge from dest to src also
	newNode=newAdjListNode(src);
	newNode->next=graph->array[dest].head;
	graph->array[dest].head=newNode;
}

// A utility function to print the adjacency list representation of graph 
void printGraph(Graph* graph){
	int v;
	for(v=0;v<graph->V;++v){
		AdjListNode* pCrawl=graph->array[v].head;
		cout<<"\n Adjacency list of vertex"<<v<<"\n head";
		while(pCrawl){
			cout<<"->"<<pCrawl->dest<<endl;
			pCrawl=pCrawl->next;
		}
		cout<<endl;
	}
}
//Driver program to test above functions
int main(){
	//create the graph given in the above figures
	int V=5;
	Graph* graph=createGraph(V);
	addEdge(graph, 0,1);
	addEdge(graph,0,4);
	addEdge(graph,1,2);
	addEdge(graph,1,3);
	addEdge(graph,1,4);
	addEdge(graph,2,3);
	addEdge(graph,3,4);
	//print the adjacency list representation of the above graph
	printGraph(graph);
	return 0;
}
