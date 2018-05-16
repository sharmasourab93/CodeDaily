package beans;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class EmploySearch {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	public ResultSet searchEmploy(int empno){
		try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin;@localhost:1521:orcl","scott","tiger");
			PreparedStatement pst=con.prepareStatement("select * from Employ where Empno=?");
			pst.setInt(1, empno);
			ResultSet rs=pst.executeQuery();
			return rs;
		}catch(ClassNotFoundException e){
			e.printStackTrace();
			return null;
		}catch(SQLException e){
			e.printStackTrace();
			return null;
		}
		
	}
}
