
public class ArrEx {
	public void arrayDemo(){
		int[] a=new int[]{12,4,667,23};
		/*for(int i=0;i<a.length;i++){
			System.out.println("\n"+a[i]);
		}*/
		for(int i:a){
			System.out.println("\n"+i );
		}
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrEx obj=new ArrEx();
		obj.arrayDemo();
	}

}
