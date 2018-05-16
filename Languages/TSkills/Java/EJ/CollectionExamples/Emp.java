
public class Emp {
	int empno;
	String name;
	double basic;
	
	public Emp() {
		
	}
	
	public Emp(int empno,String name,double basic){
		this.empno=empno;
		this.name=name;
		this.basic=basic;
	}
	
	@Override
	public String toString() {
		return "Empno " +empno+ " Name " +name+ " Basic " +basic;
	}
}
