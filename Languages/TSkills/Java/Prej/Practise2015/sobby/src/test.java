public class test {
	int i;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test obj1=new test();
		obj1.i=12;
		
		test obj2=obj1;
		obj2.i=13;
		System.out.println(obj1.i);
		System.out.println(obj2.hashCode()+ " " +obj2.hashCode() );

	}

}
