#include<iostream>
using namespace std;

class LivingThing{
	protected:
		virtual void breathe(){
			cout<<"I'm breathing as a living thing."<<endl;
		}
};

class Animal: protected LivingThing{
	protected:
		void breathe(){
			cout<<"I'm breathing as an animal"<<endl;
		}
};

class Reptile:protected LivingThing{
	//protected:
	public:
		virtual void breathe(){
			cout<<"I m breathing like a reptile"<<endl;
		}
		void crawl(){
			cout<<"I'm crawling like a reptile"<<endl;
		}
		
};

class Snake: //public Animal,public Reptile{
protected Animal,protected Reptile{
	/*public:
	void breathe(){
		cout<<"I'm snake breathing"<<endl;
	}
	void crawl(){
		cout<<"Im a crawling snake"<<endl;
	}*/
};

int main(){
	Snake snake;
	snake.breathe();
	snake.crawl();
}

