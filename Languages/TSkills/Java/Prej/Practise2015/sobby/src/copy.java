public class Max3 {
	public void check(int a,int b,int c){
		//Program to check max of 3 nos
		if(a>b && a>c){
			System.out.println(a+ " is the maximum");
		}else if(b>a && b>c){
			System.out.println(b+ " is the maximum");
		}else{
			System.out.println(c+" is the maximum");
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Max3 obj=new Max3();
		obj.check(12,3,11);
	}
}
