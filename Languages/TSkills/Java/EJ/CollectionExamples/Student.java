
public class Student {
	int sno;
	String firstName;
	String lastName;
	double gpa;
	
	public Student(int sno,String firstName,String lastName,double gpa){
		this.sno=sno;
		this.firstName=firstName;
		this.lastName=lastName;
		this.gpa=gpa;
	}
	
	@Override
	public String toString() {
return "Sno " +sno+ " First Name " +firstName+ " Last Name " +lastName + " Gpa "+gpa;
	}
}
