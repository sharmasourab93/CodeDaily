public class StEx {
	public void show(){
			System.out.println("From Show Method(General Method)");
	}
	public static void display(){
		System.out.println("Display method(Static Method)");
	}
	public static void main(String args[]){
		StEx Stex=new StEx();
		Stex.display();
	}
}
