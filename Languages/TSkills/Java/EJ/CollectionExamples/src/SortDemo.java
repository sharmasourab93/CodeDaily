import java.util.Set;
import java.util.TreeSet;

public class SortDemo {

	public static void main(String[] args) {
		Set s=new TreeSet();
		s.add("Rahil");
		s.add("Nitu");
		s.add("Akankasha");
		s.add("Mahima");
		s.add("Raghav");
		
		System.out.println("Elements of ArrayList are ");
		for(Object ob : s){
			System.out.println(ob);
		}
	}
}
