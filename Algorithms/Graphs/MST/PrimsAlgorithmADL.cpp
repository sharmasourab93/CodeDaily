//Prim's ALgorithm with Adjacency list representation
#include<iostream>
#include<climits>
#define V 5
using namespace std;
class Prims{
	public:
		struct Node{
			int dest;
			int weight;
			Node *next;
		};
		struct AdjList{
			Node *head;
		};
		struct Graph{
			int V;
			AdjList *array;
		};
		struct Node *newNode(int dest, int weight){
			Node * newnode=new Node();
			newnode->dest=dest;
			newnode->weight=weight;
			newnode->next=NULL;
			return newnode;
		}
		struct Graph *createGraph(int V){
			Graph *newgraph=new Graph();
			newgraph->V=V;
			newgraph->array=(AdjList*)malloc(V* sizeof(AdjList));
			for(int i=0;i<V;i++){
				newgraph->array[i].head=NULL;
			}
			return Graph;
		}
		void addEdge(Graph *graph,int src, int dest){
			Node *newnode=newNode(dest,weight);
			newnode->next=graph->array[src].head;
			graph->array[src].head=newnode;
			
			newnode=newNode(src,weight);
			newnode->next=graph->array[dest].head;
			graph->array[dest].head=newnode;
		}
		int minKey(int key[],bool mstSet[]){
			int min=INT_MAX,min_index;
			for(int i=0;i<V;i++){
				if(mstSet[i]==false&&key[i]<min){
					min=key[i]; min_index=i;
				}
			}
			return min_index;
		}
		void PrimsMST(int Graph){
			
		}
};
