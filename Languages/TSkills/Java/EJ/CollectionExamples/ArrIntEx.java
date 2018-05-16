import java.util.ArrayList;
import java.util.List;

public class ArrIntEx {

	public static void main(String[] args) {
		
		List alist=new ArrayList();
		alist.add(new Integer(32));
		alist.add(new Integer(8));
		alist.add(new Integer(82));
		alist.add(new Integer(31));
		alist.add(new Integer(81));
		
		int sum=0;
		
		for(Object ob : alist){
			sum+=(Integer)ob;
		}
		
		System.out.println("Sum is  " +sum);
	}
}
