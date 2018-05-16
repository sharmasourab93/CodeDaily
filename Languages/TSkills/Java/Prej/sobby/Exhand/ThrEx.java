package Exhand;
import java.io.*;
public class ThrEx {
	public void show(int n){
		boolean flag=true;
		if(n==0){
			flag=false;
			throw new NumberFormatException("Zero is invalid value..");
		}
		if(n<0){
			flag=false;
			throw new ArithmeticException("Negative nos not allowed..");
		}
		if(flag==true){
			System.out.println("N value is "+ n  );
		}
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n=5;
		ThrEx t=new ThrEx();
		try{
			t.show(n);
		}catch(ArithmeticException e){
			e.printStackTrace();
		}catch(NumberFormatException e){
			e.printStackTrace();
		}catch(Exception e){
			e.printStackTrace();
		}
	}
}
