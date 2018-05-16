//Kahn's Algorithm
#include<iostream>
#include<vector>
#include<list>
#include<queue>
using namespace std;
class Graph{
	int V;
	list<int> *adj;
	public:
	//Constructor
	 Graph(int V){
	 	this->V=V;
	 	adj=new list<int>[V];
	 }
	 //Function to add an edge to graph
	 void addEdge(int v, int w){
	 	adj[v].push_back(w);
		//Add w to v's list
	 }
	 //Print a topological sort of the complete Graph
	 void topologicalSort(){
	 	/*
		 Create a vectore to store indegrees of all 
		 vertices. Initialize all indegrees as 0.
		 */
		 vector<int> in_degree(V,0);
		 //Traverse adjacency lists to fill indegrees of vertices
		 //This step takes o(V+E) time
		 for(int u=0;u<V;u++){
		 	list<int>::iterator itr;
		 	for(itr=adj[u].begin();itr!=adj[u].end();itr++){
		 		in_degree[*itr]++;
			 }
		 }
		 //create a queue and enqueue allvertices with indegree 0
		 queue<int> q;
		 for(int i=0;i<V;i++)
		 	if(in_degree[i]==0)
		 		q.push(i);
		//Initialize count of visited vertices
		int cnt=0;
		
		//Create a vector to store result (A topological ordering of the vertices)
		vector<int> top_order;
		//One by one dequeue vertices from queue and enqueue
		//adjacents if indegree of adjacent becomes 0
		while(!q.empty()){
			//Extract front of queue(or perform dequeue)
			//and add it to topological order
			int u=q.front();
			q.pop();
			top_order.push_back(u);
			//Iterate through all its neighbouring nodes 
			//of dequeued node u and decrease their in-degree
			//by 1
			list<int>::iterator itr;
			for(itr=adj[u].begin();itr!=adj[u].end();itr++)
				//If in-degree becomes zero, add it to queue
				if(--in_degree[*itr]==0)
					q.push(*itr);
			cnt++;
			
		}
		if(cnt!=V){
			cout<<"There exists a cycle in the graph\n";
			return;
		}
		//Print Topological order
		for(int i=0;i<top_order.size(); i++)
			cout<<top_order[i]<<" ";
		cout<<endl;
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
