package test;
import java.util.Scanner;
@SuppressWarnings("serial")
/**
 * Write a program to validate email address
 * 1) first check if '@' is not found then throw InvaludEmailException
 * 2) If first part length>20 then throw InvalidEmailLengthException
 */
class InvalidEmailException extends Exception {
	public InvalidEmailException(String error){
		super(error);
	}
}
@SuppressWarnings("serial")
class InvalidEmailLengthException extends Exception{
	public InvalidEmailLengthException(String error){
		super(error);
	}
}
public class test1 {
	public static void main(String[] args) throws InvalidEmailLengthException {
		// TODO Auto-generated method stub
		Scanner scan=new Scanner(System.in);
		System.out.println("\nEnter the email id: ");
		String emailid=scan.next();
		/*if(emailid.length()>20){
			try{
				System.out.println("This is a valid email Id");
			}catch(InvalidEmailLengthException e){
				System.out.println("This is an email id with excess length.");
			}
		}else{
			
		}*/
		int k;
		boolean flag=false;
		char ch[]=emailid.toCharArray();
		for(int i=0;i<emailid.length();i++){
			try{
				if(ch[i]=='@'){
					k=i;
					flag=true;
				}
			}	
			catch(InvalidEmailException e){
				System.out.println("This email is Invalid. Doesn't contain '@'.");
			}
				
			}
		}
		
}