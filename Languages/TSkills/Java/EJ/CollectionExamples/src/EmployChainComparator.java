import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class EmployChainComparator implements Comparator {

	private List listComparators;
	
	public EmployChainComparator(Comparator...comparators){
		this.listComparators=Arrays.asList(comparators);
	}
	
	@Override
	public int compare(Object o1, Object o2) {
		Employ e1=(Employ)o1;
		Employ e2=(Employ)o2;
		
		return 0;
	}
}
