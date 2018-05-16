public class Fact {
	public void calc(int n){
		int f=1;
		while(n>=1){
			f=f*n;
			n--;
		}
		System.out.println("Factorial Value is "+f);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Fact obj=new Fact();
		obj.calc(5);

	}

}
