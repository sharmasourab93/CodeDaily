public class VarArgsDemo {
	public void show(String...name){
		for(String s:name){
				System.out.print(s +" ");
		}
		System.out.println();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		VarArgsDemo obj=new VarArgsDemo();
		obj.show();
		obj.show("Prasanna");
		obj.show("Kiran","Salman");
		obj.show("Kiran","Salman","Sourab");
	}

}
