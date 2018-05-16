import java.util.Vector;

public class VectorDemo {

	public static void main(String[] args) {
		Vector v=new Vector(3,2);
		System.out.println("Size " +v.size());
		System.out.println("Capacity "+v.capacity());
		
		v.addElement("Nitu");
		v.addElement("Akankasha");
		v.addElement("Rahil");
		System.out.println("Size " +v.size());
		System.out.println("Capacity "+v.capacity());
		
		v.add("Raghav");
		System.out.println("Size " +v.size());
		System.out.println("Capacity "+v.capacity());
		System.out.println(v);
	}
}
