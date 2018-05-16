import java.util.ArrayList;
import java.util.List;

public class ArrListDemo {

	public static void main(String[] args) {
		List alist=new ArrayList();
		
		alist.add("Nitu");
		alist.add("Akankasha");
		alist.add("Mahima");
		alist.add("Rahil");
		alist.add("Raghav");
		
		System.out.println("Elements of ArrayList are ");
		for(Object ob : alist){
			System.out.println(ob);
		}
		
		alist.add(3,"Krishna");
		System.out.println("List after adding new element");
		for(Object ob : alist){
			System.out.println(ob);
		}
		
		alist.set(2,"Singh");
		System.out.println("List after modifying element ");
		for(Object ob : alist){
			System.out.println(ob);
		}
		
		alist.remove(3);
		System.out.println("List after removing element by Index");
		for(Object ob : alist){
			System.out.println(ob);
		}
		alist.remove("Rahil");
		System.out.println("List after removing element by Obj. Name ");
		for(Object ob : alist){
			System.out.println(ob);
		}
		
	}
}
