//Partition Vector
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
	vector<int> vect()={2,1,5,6,8,7};
	is_partitioned(vect.begin(),vect.end(),[](int x){
		return x%2==0;
	})? cout<<"Vector is paritioned":cout<<"Vector is not partitioned";
	partition(vect.begin(),vect.end(),[](int x){
		return x%2==0;
	});
	for(int &x:vect) cout<<x<<" ";
	return 0;
}
