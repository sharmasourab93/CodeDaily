import java.util.ArrayList;
import java.util.List;

public class ArrEmp {
	public static void main(String[] args) {
		List alist=new ArrayList();
		alist.add(new Emp(1,"Nitu",58222));
		alist.add(new Emp(2,"Akankasha",84112));
		alist.add(new Emp(3,"Rahil",82454));
		alist.add(new Emp(4,"Mahima",48145));
		alist.add(new Emp(5,"Raghav",82444));
		
		System.out.println("Employ Data is ");
		for(Object ob : alist){
			Emp e=(Emp)ob;
			System.out.println(e);
		}
	}
}
