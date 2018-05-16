package AbstractDemo;

abstract class Student{
	int sno;
	String name;
	public Student(int sno,String name){
			this.sno=sno;
			this.name=name;
	}
	public String toString(){
		return "Sno "+sno+" Name "+name;
	}
}
class Kandarp extends Student{

	public Kandarp(int sno, String name) {
		super(sno, name);
		// TODO Auto-generated constructor stub
	}		
}
class Sourab extends Student{

	public Sourab(int sno, String name) {
		super(sno, name);
		// TODO Auto-generated constructor stub
	}
}
public class AbsC {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Kandarp k=new Kandarp(1,"kandarpa");
		Sourab s=new Sourab(2,"Srikanth");
		Student[] sarr=new Student[]{k,s};
		for (Student x:sarr){
			System.out.println(x);
		}
	}

}
