import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class EmploySearch {

	/**
	 * @param args
	 */
	public static void main(String[] args) throws SQLException{
		// TODO Auto-generated method stub
		try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
			System.out.println("Enter Employ No ");
			Scanner scr=new Scanner(System.in);
			int empno=scr.nextInt();
			PreparedStatement pst=con.prepareStatement("Select * from Employ where Empno=?");
			pst.setInt(1,empno);
			ResultSet rs=pst.executeQuery();
			if(rs.next()){
				System.out.println("Empno "+rs.getInt("empno"));
				System.out.println("Name "+rs.getString("name"));
				System.out.println("Department "+rs.getString("job"));
				System.out.println("Designation "+rs.getString("Desig"));
				System.out.println("Basic "+rs.getInt("Basic"));
			}else{
				System.out.println("Record not found!");
			}
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}
	}

}
