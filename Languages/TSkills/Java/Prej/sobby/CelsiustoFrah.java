import java.util.Scanner;
public class CelsiustoFrah {
	void CeltoFrah(double cel){
		double frah=((cel*(9/5)) + 32);
		System.out.println(cel+" Degrees after converting to Frahrenheit "+frah);
	}
	void FrahtoCel(double frah){
		double cel=((frah-32)*(5/9));
		System.out.println(frah+"�F after converting to Celsius"+cel); 
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan=new Scanner(System.in);
		double x1=scan.nextDouble();
		double y1=scan.nextDouble();
		int option;
		CelsiustoFrah cf=new CelsiustoFrah();
		System.out.println("Choose any of the 2:- \n\t1.Celsius \n\t2.Frahrenheit");
		option=scan.nextInt();
		if(option==1){
			cf.CeltoFrah(x1);
		}else{
			cf.FrahtoCel(y1);
		}
	}

}
