package AbstractDemo;

abstract class Animal{
		abstract void name();
		abstract void type();
}
class Lion extends Animal{
	public void name(){
		System.out.println("I am lion");
	}
	public void type(){
		System.out.println(" I am a Mamal");
	}
}
class zebra extends Animal{
	public void name(){
		System.out.println(" I am a zebra");
	}
	public void type(){
		System.out.println("I am a herbivore");
	}
}
public class AbsDemo {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Animal a1=new Lion();
		Animal a2=new zebra();
		Animal arr[]={new Lion(),new zebra()};
		for(Animal t:arr){
			t.name();
			t.type();
		}
	}
}
