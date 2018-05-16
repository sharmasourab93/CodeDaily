import java.util.HashSet;
import java.util.Set;

public class HsetDemo {

	public static void main(String[] args) {
		Set s=new HashSet();
		s.add("SAlman");
		s.add("Kandarp");
		s.add("Shwta");
		s.add("Kandarp");
		s.add("Salman");
		s.add("Shwetha");
		s.add("SAlman");
		s.add("Kandarp");
		s.add("Shwta");
		s.add("Kandarp");
		s.add("Salman");
		s.add("Shwetha");
		s.add("SAlman");
		s.add("Kandarp");
		s.add("Shwta");
		s.add("Kandarp");
		s.add("Salman");
		s.add("Shwetha");
		for(Object ob : s){
			System.out.println(ob);
		}
		
	}
}
