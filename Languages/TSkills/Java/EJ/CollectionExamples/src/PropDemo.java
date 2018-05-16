import java.util.Properties;
import java.util.Scanner;

public class PropDemo {

	public static void main(String[] args) {
		Properties p=new Properties();
		p.put("Nitu","Singhal");
		p.put("Rahil","Sharma");
		p.put("Raghav","Sharma");
		p.put("Mahima","Kaur");
		String key,value;
		System.out.println("Enter Key and Value ");
		Scanner scr=new Scanner(System.in);
		key=scr.nextLine();
		value=scr.nextLine();
		
		String res=p.getProperty(key,"Not Found");
		if(res.equals(value)){
			System.out.println("Correct Credentials...");
		}
		else {
			System.out.println("Invalid Credentials...");
		}
	}
}
