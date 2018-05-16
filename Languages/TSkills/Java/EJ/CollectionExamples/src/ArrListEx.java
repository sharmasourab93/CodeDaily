import java.util.ArrayList;
import java.util.List;

public class ArrListEx {

	public List arrListDemo(int empno){
		List alist=new ArrayList();
		if(empno==1){
			alist.add("Rahil");
			alist.add("Sharma");
			alist.add("Jammu");
		}
		else if(empno==2){
			alist.add("Raghav");
			alist.add("Official");
			alist.add("Jammu");
		}
		else {
			alist.add("Not Found");
		}
		return alist;
	}
	
	public static void main(String[] args) {
		ArrListEx obj=new ArrListEx();
		List alist=obj.arrListDemo(2);
		for(Object ob : alist){
			System.out.println(ob);
		}
	}
}
