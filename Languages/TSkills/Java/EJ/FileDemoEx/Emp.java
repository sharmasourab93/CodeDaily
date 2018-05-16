import java.io.Serializable;
public class Emp implements Serializable {
	int empno;
	String name;
	double basic;
	/**
	 * @param args
	 */
	public Emp(int empno,String name,double basic) {
		// TODO Auto-generated method stub
		this.empno=empno;
		this.name=name;
		this.basic=basic;
	}
	public String toString(){
		return "Empno "+empno+" Name "+" Basic "+basic;
	}
}
