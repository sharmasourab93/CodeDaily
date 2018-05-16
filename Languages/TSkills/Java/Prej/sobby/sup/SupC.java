package sup;
class Emp{
		int empno;
		String name;
		double basic;
		public Emp(int empno,String name,double basic){
				this.empno=empno;
				this.name=name;
				this.basic=basic;
		}
		@Override
	public String toString(){
			return "Empno "+ empno+" Name "+name+" Basic "+basic;
	}
}
class Sravan extends Emp{

	public Sravan(int empno, String name, double basic) {
		super(empno, name, basic);
		// TODO Auto-generated constructor stub
	}
		
}
public class SupC {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Sravan n=new Sravan(1,"Sravan",63344);
		System.out.println(n);
	}

}
