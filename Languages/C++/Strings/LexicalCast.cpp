//Converting String to num and viceversa
#include<iostream>	//j
#include<string>	//For string
#include<boost/lexical_cast.hpp>	//for lexical_cast()
using namespace std;
int main(){
	string str="5";
	string str1="6.5";
	//Initializing f_value with casted float
	float f_value=boost::lexical_cast<float>(str1);
	//Initializing i_value with casted int
	int i_value=boost::lexical_cast<int>(str);
	//Displaying casted values
	cout<<"The float value after casting is:";
	cout<<f_value<<endl;
	cout<<"the int value after casting is: "<<i_value<<endl;
}
