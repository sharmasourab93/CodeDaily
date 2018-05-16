import java.util.Scanner;

public class Scan2 {
	public static void main(String[] args) {
		int a,b;
		System.out.println("Enter 2 Nos  ");
		Scanner scr=new Scanner(System.in);
		a=scr.nextInt();
		b=scr.nextInt();
		int c=a+b;
		System.out.println("Sum is  " +c);
	}
}
