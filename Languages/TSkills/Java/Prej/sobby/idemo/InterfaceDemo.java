package idemo;
interface Data{
	void name();
	void email();
}
class Shwtha implements Data{

	@Override
	public void name() {
		// TODO Auto-generated method stub
		System.out.println("Name is Shwtha");
	}

	@Override
	public void email() {
		// TODO Auto-generated method stub
		System.out.println("Emails suck! Whatsapp...........");
	}
	
}
class Kiran implements Data{

	@Override
	public void name() {
		// TODO Auto-generated method stub
		System.out.println("Kiran WTH!!!!!");
	}

	@Override
	public void email() {
		// TODO Auto-generated method stub
		System.out.println("Email for kiran doesnt exist ");
	}
	
}
public class InterfaceDemo {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Data[] arr=new Data{new Kiran(),new Shwtha()};
		for(Data d:arr){
			d.name();
			d.email();
		}
	}

}
