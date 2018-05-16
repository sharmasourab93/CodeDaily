#include<bits/stdc++.h>
using namespace std;
map<pair<int,int>,int> vis;
void printPositions(int a[3][3]){
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			if(vis[{i,j}]==0){
				cout<<"("<<i<<", "<<j<<" )"<<"\n";
			}
		}
	}
}
int main(){
	int mat[3][3]={{0,1,2},{3,4,5},{6,7,8}};
	vis[{0,0}]=1;
	vis[{1,0}]=1;
	vis[{1,1}]=1;
	vis[{2,2}]=1;
	printPositions(mat);
}

