import java.util.LinkedList;
import java.util.List;

public class LinkedListDemo {
	public static void main(String[] args) {
		List lst=new LinkedList();
		lst.add("Mahima");
		lst.add("Nitu");
		lst.add("Akankasha");
		lst.add("Rahil");
		lst.add("Raghav");
		
		for(Object ob : lst){
			System.out.println(ob);
		}
	}
}
