import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;

public class StudentDemo {
	public static void main(String[] args) {
		//Comparator c=new NameComparator();
		Comparator c=new GpaComparator();
		Set s=new TreeSet(c);
		s.add(new Student(1,"Rahil","Sharma",4.5));
		s.add(new Student(2,"Nitu","Singhal",4.2));
		s.add(new Student(3,"Raghav","Sharma",4.8));
		s.add(new Student(4,"Mahima","Kour",4.9));
		
		for(Object ob : s){
			System.out.println(ob);
		}
	}
}
