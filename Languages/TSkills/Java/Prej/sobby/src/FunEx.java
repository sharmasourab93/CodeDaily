public class FunEx {
	public void show(int x){
		System.out.println("Show Method with Integer parameter...");
	}
	public void show(double x){
		System.out.println("Show Method with double parameter...");
	}
	public void show(String x){
			System.out.println("Show method with String Parameter...");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FunEx obj=new FunEx();
		obj.show(52);
		obj.show(12.66);
		obj.show("raj");
	}
}