public class CalcDemo {
	public int Sum(){
		return 10;
	}
	public int sum(int x){
		return x+12;
	}
	public int sum(int x,int y){
		return x+y;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int res;
		CalcDemo obj=new CalcDemo();
		res=obj.sum(63,54);
		System.out.println(res);
		
		res=obj.Sum();
		System.out.println(res);
		
		res=obj.sum(52);
		System.out.println(res);
	}

}
