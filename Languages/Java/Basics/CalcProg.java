/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Basics;

/**
 *
 * @author esoussh
 */
public class CalcProg {
	public void calc(int a,int b){
			int c=a+b;
			System.out.println("Sum is "+c);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a,b;
		a=Integer.parseInt(args[0]);
		b=Integer.parseInt(args[1]);
		CalcProg obj=new CalcProg();
		obj.calc(a,b);
	}
}
