
public class EvenOdd {

	/**
	 * @param args
	 */
	public void check(int n){
		if(n%2==0){
			System.out.println("Even No...");
		}else{
			System.out.println("Odd no...");
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		EvenOdd obj=new EvenOdd();
		obj.check(12);
	}

}
