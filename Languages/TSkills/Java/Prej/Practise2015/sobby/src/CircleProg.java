public class CircleProg {
	public void calc(double radius){
		double r2=radius * radius;
		double pi=(22/7);
		double area= pi* r2;
		double circum=(2*pi*radius);
		System.out.println("Area of the circle "+ area+"Sqmt");
		System.out.println("Circumference of the circle "+ circum+"mts");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double radius= Double.parseDouble(args[0]);
		CircleProg obj=new CircleProg();
		obj.calc(radius);
	}

}
