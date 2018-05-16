import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.sql.DataSource;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.jdbc.datasource.DriverManagerDataSource;


public class MainProg {

	public static void main(String[] args) throws SQLException {
		ApplicationContext context=new ClassPathXmlApplicationContext("jdbc.xml");
		DataSource dataSource=(DriverManagerDataSource)context.getBean("dataSource");
		Connection con=(Connection)dataSource.getConnection();
		String cmd="insert into Employ values(?,?,?,?,?)";
		PreparedStatement pst=con.prepareStatement(cmd);
		pst.setInt(1,53);
		pst.setString(2,"Harish");
		pst.setString(3,"Java");
		pst.setString(4,"Programmer");
		pst.setInt(5,58666);
		pst.executeUpdate();
		System.out.println("*** Record Inserted ***");
	}
}
