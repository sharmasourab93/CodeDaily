	class Emp{
			int empno;
			String name;
			double basic;
			
			public Emp(){
					empno=1;
					name="Keerthi";
					basic=58232;
			}
			@Override
			public String toString(){
				return "Empno "+empno+ " Name "+ name + " Basic "+ basic;
			}
	}
public class ConDemo {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Emp e=new Emp();
		System.out.println(e); 
	}

}
