public class PrimeEx {
	public void check(int n){
		boolean flag=false;
		for(int i=2;i<n;i++){
			if(n%i==0){
				flag=true;
			}
		}
		if(flag==true){
			System.out.println("Not prime!");
		}else if(n==1){
			System.out.println("1 is neither prime nor composite!");
		}
		else{
			System.out.println("Prime!");
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PrimeEx obj=new PrimeEx();
		obj.check(37);
	}

}
