public class Student {

	/**
	 * @param args
	 */
	int sno;
	String name;
	char grade;
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "Sno "+sno+" Name "+name+" Grade "+grade;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Student obj=new Student();
		obj.sno=1;
		obj.name="Kandarpa";
		obj.grade='A';
		System.out.println(obj);
	}

}
