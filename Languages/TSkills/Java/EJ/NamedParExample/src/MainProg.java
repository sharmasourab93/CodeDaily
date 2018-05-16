import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainProg {
	public static void main(String[] args) {
		ApplicationContext context=new 
				ClassPathXmlApplicationContext("jdbc.xml");
		DataInsertDao d=(DataInsertDao)context.getBean("myDao");
		d.insertRecord();
	}
}
