package sup;
class First{
	public void show(){
		System.out.println("Show Method from class First");
	}
	
}
class Second extends First{
		public void show(){
				super.show();
				System.out.println("Show method from class Second...");
		}
}
public class SupEx {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Second x=new Second();
		x.show();
		
	}

}
