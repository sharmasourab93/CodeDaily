//A Simple DFS Function 
#include<iostream>
#include<list>
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
	void addEdge(int src, int dest){
		adj[src].push_back(dest);
	}
	void DFSUtil(int V,bool visited[]){
		visited[V]=true;
		cout<<V<<" ";
		list<int>::iterator i;
		for(i=adj[V].begin();i!=adj[V].end();++i){
			if(!visited[*i]){
				DFSUtil(*i,visited);
			}

		}
	}
	void DFS(int v){
		bool visited[V];
		for(int i=0;i<v;i++){visited[i]=false;}
		DFSUtil(v, visited);
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
    cout << "Following is Breadth First Traversal "
         << "(starting from vertex 2) \n";
    g.DFS(2);
 
    return 0;
}
