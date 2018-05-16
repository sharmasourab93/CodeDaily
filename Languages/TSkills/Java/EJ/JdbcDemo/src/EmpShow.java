import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class EmpShow {
	
	public static void main(String[] args) throws SQLException {
		// TODO Auto-generated method stub
		try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
			Statement st=con.createStatement();
			ResultSet rs=st.executeQuery("select * from emp");
			while(rs.next()){
				System.out.println("Employ No"+rs.getInt("Empno"));
				System.out.println("Name "+rs.getString("Ename"));
				System.out.println("Job "+rs.getString("Job"));
				System.out.println("Salary "+rs.getInt("Sal"));
				System.out.println("Department No "+rs.getInt("DeptNo"));
			}
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}
		

	}

}
