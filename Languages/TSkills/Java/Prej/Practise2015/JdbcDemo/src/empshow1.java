import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class empshow1 {
	public static void main(String[] args) throws SQLException{
		// TODO Auto-generated method stub
		try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
			Statement st=con.createStatement();
			ResultSet rs=st.executeQuery("select * from employ");
			while(rs.next()){
				System.out.println("Employ No "+rs.getInt("empno"));
				System.out.println("Name "+rs.getString("name"));
				System.out.println("Dept "+rs.getString("Dept"));
				System.out.println("Desig "+rs.getInt("Desig"));
				System.out.println("Basic "+rs.getInt("Basic"));
			}
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}
	}

}
