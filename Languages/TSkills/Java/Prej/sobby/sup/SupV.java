package sup;
class C1{
	int i;
}
class C2 extends C1{
	int i;
	public C2(int a,int b){
		this.i=a;
		super.i=b;
	}
	@Override
	public String toString(){
		return "Base class i "+super.i+" Derived Class i "+this.i;
	}
}
public class SupV {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		C2 x =new C2(11,31);
		System.out.println(x);
		
	}

}
