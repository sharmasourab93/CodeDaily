package Inheritance;

class C1{
	static {
		System.out.println("Base Class static constructor");
	}
	public C1(){
		System.out.println("Base Class Constructor...");
	}
}
class C2 extends C1{
	static{
			System.out.println("Derived Class Static constructor...");
	}
	public C2(){
			System.out.println("Derived Class Constructor...");
	}
}
public class Inhc {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		C2 obj=new C2();
	}
}
