import java.util.TreeSet;

public class CustomerDemo {

	public static void main(String[] args) {
		Customer c1=new Customer(1,"Nitu",5233);
		Customer c2=new Customer(2,"Akankasha",4845);
		Customer c3=new Customer(3,"Rahil",4221);
		Customer c4=new Customer(4,"Mahima",4111);
		
		TreeSet ts=new TreeSet();
		ts.add(c1);
		ts.add(c2);
		ts.add(c3);
		ts.add(c4);
		
		for(Object ob : ts){
			Customer c=(Customer)ob;
			System.out.println(c);
		}
	}
}
