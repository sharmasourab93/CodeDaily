public class CalcProg {
	public void calc(int a,int b){
			int c=a+b;
			System.out.println("Sum is "+c);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a,b;
			a=Integer.parseInt(args[0]);
			b=Integer.parseInt(args[1]);
			CalcProg obj=new CalcProg();
			obj.calc(a,b);
	}
}
