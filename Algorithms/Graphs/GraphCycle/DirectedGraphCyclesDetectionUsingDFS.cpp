//Detecting cycles in a Directed Graph using DFS
//Refered to Geeks for geeks
#include<iostream>
#include<list>
using namespace std;
class Graph{
	int V;
	list<int> *adj;
	public:
		Graph(int V){
			this->V=V;
			adj=new list<int> [V];
		}
		void addEdge(int src, int dest){
			adj[src].push_back(dest);
		}
		void DFSCyclicUtil(int v, bool visited[],bool *recStack){
			visited[v]=true;
			recStack[v]=true;
			list<int>::iterator i;
			for(i=adj[v].begin();i!=adj[v].end();++i)
				if(!visited[*i]&& DFSCyclicUtil(i,*visited,*recStack)) return true;
				else if(recStack[*i]) return true;
		}
		void DFSCyclic(){
			bool *visited=new bool[V];
			bool *recStack=new bool[V];
			for (int i=0;i<V;i++) 
				visited[i]=false; 
				recStack[i]=false;
			for(int j=0;j<V;j++)
				if(DFSCyclicUtil(i,visited,recStack))
					return true;
			return false;
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
    cout << "\nDetecting cycle in a graph:"<<endl;
    if(g.DFSCyclic())
    	cout<<"Cyclic"<<endl;
    else
    	cout<<"Not cyclic"<<endl;
    return 0;
}

