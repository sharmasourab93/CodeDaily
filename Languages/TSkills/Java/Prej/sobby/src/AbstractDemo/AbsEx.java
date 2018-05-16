package AbstractDemo;
abstract class Training{
		abstract void preTest();
		abstract void postTest();
}
class Sourab extends Training{
	@Override
	void preTest() {
		// TODO Auto-generated method stub
		System.out.println("Kavya Scored 80% in PreTest");
	}
	@Override
	void postTest() {
		// TODO Auto-generated method stub
		System.out.println("Kavya scored 84% in Post test");
	}
}
class Salman extends Training{
	@Override
	void preTest() {
		// TODO Auto-generated method stub
		System.out.println("Salman scored 89% in Pretest...");
	}
	@Override
	void postTest() {
		// TODO Auto-generated method stub
		System.out.println("Salman scored 84% in Post test");
	}
}
public class AbsEx {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Training obj1=new Sourab();
		Training obj2=new Salman();
		Training[] arr=new Training[]{new Salman(),new Sourab()};
		for(Training t:arr){
			t.preTest();
			t.postTest();
		}
	}

}
