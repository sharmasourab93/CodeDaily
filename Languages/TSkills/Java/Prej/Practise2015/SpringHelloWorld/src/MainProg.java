import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;


public class MainProg {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Resource res=new ClassPathResource("Hello.xml");
		BeanFactory factory=new XmlBeanFactory(res);
		Hello h=(Hello)factory.getBean("hello");
		System.out.println(h.sayHello("Sourab"));
	}
}
