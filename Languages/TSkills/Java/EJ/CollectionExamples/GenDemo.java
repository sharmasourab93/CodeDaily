class Test<T>{
	public void swap(T x,T y){
		T t;
		t=x;
		x=y;
		y=t;
		System.out.println("X "+x+" Y "+y);
	}
}
public class GenDemo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Test obj=new Test();
		int x=12,y=13;
		double d1=12.5,d2=566.23;
		String s1="Sourab",s2="Kiran";
		obj.swap(x,y);
		obj.swap(d1, d2);
		obj.swap(s1,s2);
	}

}
