//Depth First Search
//Code from Geeks4 geeks
#include<iostream>
#include<list>
using namespace std;
//class graph
class Graph{
	int V;
	//A List datatype
	list<int> *adj;
	public:
		//Constructor initialization
		Graph(int V){
			this->V=V;
			adj=new list<int>[V];
		}
		//Function to add edges to map the adjacency list
		void addEdge(int v, int w){
			adj[v].push_back(w);
		}
		//A utility recursive function which marks a node visited and traverses further
		void DFSUtil(int V, bool visited[]){
			visited[V]=true;
			cout<<V<<" ";
			list<int>::iterator i;
			for( i=adj[V].begin();i!=adj[V].end();++i){
				if(!visited[*i])
				{
					//Recursive call
					DFSUtil(*i, visited);
				}
			}
		}
		//A primary DFS function which calls the recursive DFSUtil
		void DFS(int V){
			bool *visited=new bool[V];
			for(int i=0;i<V;i++) visited[i]=false;
			DFSUtil(V,visited);
		}
};
int main(){
	Graph g(4);
	g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    cout << "Following is Depth First Traversal "
         << "(starting from vertex 2) \n";
    g.DFS(2);
    return 0;
}
