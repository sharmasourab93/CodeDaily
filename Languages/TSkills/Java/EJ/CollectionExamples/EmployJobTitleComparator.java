import java.util.Comparator;

public class EmployJobTitleComparator implements Comparator {

	@Override
	public int compare(Object o1, Object o2) {
		Employ e1=(Employ)o1;
		Employ e2=(Employ)o2;
		return e1.getJobTitle().compareTo(e2.getJobTitle());
	}
}