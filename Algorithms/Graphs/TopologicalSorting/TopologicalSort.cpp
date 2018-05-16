//Topological Sort
#include<iostream>
#include<list>
#include<stack>
using namespace std;
class Graph{
	int V;//No. of vertices
	list<int> *adj;
	public:
	//Constructor
	 Graph(int V){
	 	this->V=V;
	 	adj=new list<int>[V];
	 }
	 //Function to add an edge to graph
	 void addEdge(int v, int w){
	 	adj[v].push_back(w);//Add w to v's list
	 }
	 //A recursive utility function
	 void topologicalSortUtil(int v, bool visited[], stack<int> &Stack){
		//Mark the current Node as visited
		visited[v]=true;
		//Recur for all the vertices adjacent to this vertex
		list<int>:: iterator i;
		for(i=adj[v].begin();i!=adj[v].end();++i){
			if(!visited[*i]){
				topologicalSortUtil(*i,visited,Stack);
			}
		}
		//Push current vertex to stack which stores result
		Stack.push(v);
	}
	 //Print a topological sort of the complete Graph
	 void topologicalSort(){
	 	stack<int> Stack;
	 	//Mark all the vertices as not Visited
	 	bool *visited=new bool[V];
	 	for(int i=0;i<V;i++){
	 		visited[i]=false;
	 	}
	 	//call the recursive helper function to store topological 
	 	//Sort starting from all vertices one by one 
	 	for(int i=0;i<V;i++){
	 		if(visited[i]==false){
	 			topologicalSortUtil(i,visited,Stack);
	 		}
	 	}
	 	//Print contents of Stack
	 	while(Stack.empty()==false){
	 		cout<<Stack.top()<<" ";
	 		Stack.pop();
	 	}
	 }

};
//Driver program to test above functions 
int main(){
	Graph g(6);
	g.addEdge(5,2);
	g.addEdge(5,0);
	g.addEdge(4,0);
	g.addEdge(4,1);
	g.addEdge(2,3);
	g.addEdge(3,1);
	cout<<"Following is a Topological Sort of the given Graph \n";
	g.topologicalSort();
	return 0;
}