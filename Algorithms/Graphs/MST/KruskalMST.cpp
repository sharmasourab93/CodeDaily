//Kruskal's Minimum Spanning tree
//Reference from Geeks for Geeks
#include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;
// A structure to represent a weighted edge in graph
struct Edge{
	int src, dest;
};
//A structre to represent a connected, undirected and weighted graph
struct Graph{
	//V->Number of vertices, E->number of edges
	int V,E;
	//Graph is represented as an array of edges. Since the graph is 
	//undirected, the edge from src to dest is also edge from dest
	//to src. Both are counted as 1 edge here
	Edge* edge;
};
struct Graph *createGraph(Graph* graph){
	Graph *graph=(Graph*)malloc(sizeof(Graph));
	graph->V=V;
	graph->E=E;
	graph->edge=(Edge*)malloc(graph->E* sizeof(Edge));
	return graph;
}
struct subset{
	int parent;
	int rank;
};

int find(struct subset subsets[],int i){
	if(subsets[i].parent!=i){
		subsets[i].parent=find(subsets,subsets[i].parent);
	}
	return subsets[i].parent;
}

void Union(struct subset subsets[], int x, int y){
	int xroot=find(subsets,x);
	int yroot=find(subsets,y);
	if(subsets[xroot].rank<subsets[yroot].rank) subsets[xroot].parent=yroot;
	else if(subsets[xroot].rank>subsets[yroot].rank) subsets[yroot].parent=xroot;
	
	else{
		subsets[yroot].parent=xroot;
		subsets[xroot].rank++;
	}
}
int myComp(const void* a, const void* b){
	struct Edge* a1=(struct Edge*)a;
	struct Edge* b1=(struct Edge*)b;
	return a1->weight>b1->weight;
}
void KruskalMST(Graph* graph){
	int V=graph->V;
	struct Edge result[V];
	int e=0;
	int i=0;
	qsort(graph->edge,graph->E,sizeof(graph->edge[0]),myComp);
	struct subset *subsets=(struct subset*)malloc(V* sizeof(struct subset));
	for(int v=0;v<V;++v){
		subsets[v].parent=v;
		subsets[v].rank=0;
	}
	while(e<V-1){
		struct Edge next_edge=graph->edge[i++];
		int x=find(subsets, next_edge.src);
		int y=find(subsets, next_edge.dest);
	
		result[e++]=next_edge;
		if(x!=y){
			Union(subsets,x,y);
		}
		//Else Discard the next_edge
	}
	//print the contents of result[] to display the built MST
	cout<<"\nFollowing are the edges in the constructed MST\n"<<endl;
	for(i=0;i<e;++i){
		cout<<result[i].src<<" ---"<<result[i].dest<<"=="<<result[i].weight;
		return;
	}	
	
}
