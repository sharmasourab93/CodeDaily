package Exhand;

public class AssertDemo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int basic=15000;
		for(int i=0;i<6;i++){
			basic=basic+4000;
			assert basic<25000;//type '-ea' stands for enable assertion
			System.out.println(basic);
		}
	}

}
