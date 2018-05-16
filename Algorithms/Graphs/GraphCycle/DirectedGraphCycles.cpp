//Detect Cycle in an Directed Graph Using BFS
//Logic applied by self
#include<iostream>
#include<list>
using namespace std;
/* Graph Structure contains cycle like
	0->2->0, 0->1->2->0, 3->3 */
//Primary Class which derives the graph
class Graph{
	int V;
	list<int> *adj;
	public:
		//Graph constructor which initializes the number of nodes in a graph
		Graph(int V){
			this->V=V;
			adj=new list<int>[V];
		}
		//Adds edges between the nodes
		void addEdge(int src,int dest){
			adj[src].push_back(dest);
		}
		//A utility function which detects a cycle in a graph
		//A cycle also means graph either point to self or forming a loop
		bool cycle(int node){
			bool *visited=new bool[V];
			for(int i=0;i<V;i++) visited[i]=false;
			
			list<int> queue;
			visited[node]=true;
			queue.push_back(node);
			
			list<int>::iterator i;
			while(!queue.empty()){
				node=queue.front();
				queue.pop_front();
				for(i=adj[node].begin();i!=adj[node].end();++i){
					if(!visited[*i])
					{
						visited[*i]=true;
						queue.push_back(*i);
					}else{
						cout<<"\nCycle exists"<<endl;
						return true;
					}
				}
			}
			cout<<"\nCycle doesn't exist"<<endl;
			return false;
		}
};
int main(){
	Graph g(4);
	g.addEdge(0, 1);
    g.addEdge(0, 2);
    //g.addEdge(1, 2);
    //g.addEdge(2, 0);
    g.addEdge(2, 3);
    //g.addEdge(3, 3);
    cout << "\nDetecting cycle in a graph:"<<endl;
    g.cycle(0);
    return 0;
}
