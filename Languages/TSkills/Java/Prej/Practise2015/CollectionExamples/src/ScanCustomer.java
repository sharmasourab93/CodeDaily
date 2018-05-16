import java.util.Scanner;

public class ScanCustomer {
	public static void main(String[] args) {
		Customer c=new Customer();
		System.out.println("Enter Customer ID, Name and Cost ");
		Scanner scr=new Scanner(System.in);
		c.setCustId(Integer.parseInt(scr.nextLine()));
		c.setName(scr.nextLine());
		c.setCost(Integer.parseInt(scr.nextLine()));
		
		System.out.println(c);
	}
}
