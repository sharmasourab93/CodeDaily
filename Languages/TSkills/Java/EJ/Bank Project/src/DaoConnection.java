import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class DaoConnection {

	/**
	 * @param args
	 */
	public static Connection getConnection(){
		try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
			return con;
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}catch(SQLException e){
			e.printStackTrace();
		}
		return null;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
