import java.sql.Connection;
import java.util.Scanner;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
public class UserAuth {

	/**
	 * @param args
	 */
	public static void main(String[] args) throws SQLException{
		// TODO Auto-generated method stub
		String user,pwd;
		System.out.println("Enter UserName and Password: ");
		Scanner scan=new Scanner(System.in);
		try{
		user=scan.nextLine();
		pwd=scan.nextLine();
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
		PreparedStatement pst=con.prepareStatement("select * from Isers where"+ "username=? AND Password");
		pst.setString(1,user);
		pst.setString(2,pwd);
		ResultSet rs=pst.executeQuery();
		if(rs.next()){
			System.out.println("Correct Credentials...");
		}else{
			System.out.println("Invalid Credentials");
			}
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}
	}
}
