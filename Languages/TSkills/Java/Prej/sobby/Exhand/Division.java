package Exhand;
public class Division {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
		int a,b,c;
		a=Integer.parseInt(args[0]);
		b=Integer.parseInt(args[1]);
		c=a/b;
		System.out.println("Divison "+c);
		}catch(ArrayIndexOutOfBoundsException e){
			System.out.println("Please pass Arguments");
		}catch(Exception e){
			e.printStackTrace();
		}finally{
			System.out.println( "Code by Ericsson batch");
		}
	}
 }