package Exhand;

public class ArrEx {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a=new int[]{12,5};
		try{
				a[10]=55;
		}catch(ArrayIndexOutOfBoundsException e){
			System.out.println("Array size is small...");
		}catch(Exception e){
			e.printStackTrace();
		}
	}

}
