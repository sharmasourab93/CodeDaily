//Naive Pattern Searching Algorithm 
#include<iostream>
#include<string.h>
using namespace std;
//Naive Pattern Class
class Naive{
	public:
		//Naive Search Function
		void search(string text,string pat){
			int m=pat.length();
			int n=text.length();
			cout<<"\nPattern Length "<<m<<"\t"<<"Text length "<<n<<endl;
			cout<<"Text: "<<text<<"\t"<<"Pattern: "<<pat<<endl;
			for(int i=0;i<=n-m;i++){
				int j;
				//Primary Comparison of the Sample text with Pattern
				for(j=0;j<m;j++)
					if(text[i+j]!=pat[j])
						break;
				//Implies that j loop has traversed to the last instance of the pattern, 
				//and all comparisons are matching
				if(j==m)
					cout<<"Instance found at: "<<i+1<<endl;
			}
		}
};
int main(){
	Naive n;
	string text="AABAACAAADAABAA";
	//string text="AAAAAAAAAAAAAAAAAAB";
	string pattern="AABA";
	n.search(text,pattern);
}
