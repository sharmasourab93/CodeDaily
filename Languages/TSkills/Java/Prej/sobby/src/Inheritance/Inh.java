package Inheritance;
class First{
	public void show(){
		System.out.println("Show method from Class first.");
	}
}
class Second extends First{
		public void display(){
				System.out.println("Display method from class Second...");
		}
}
public class Inh {
	public static void main(String args[]){
		Second obj=new Second();
		obj.display();
		obj.show();
	}
}
