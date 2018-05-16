import java.util.Scanner;
import java.sql.*;
public class EmpUpdate {

	/**
	 * @param args
	 */
	public static void main(String[] args) throws SQLException{
		// TODO Auto-generated method stub
		int empno,basic;
		String desig;
		System.out.println("Enter Empno,desig and basic");
		Scanner scan=new Scanner(System.in);
		empno=Integer.parseInt(scan.nextLine());
		desig=scan.nextLine();
		basic=Integer.parseInt(scan.nextLine());
		try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
			PreparedStatement pst=con.prepareStatement("Update Employ set Desig=?,"+ "Basic=? where Empno=?");
			pst.setString(1,desig);
			pst.setInt(2,basic);
			pst.setInt(3,empno);
			pst.executeUpdate();
			System.out.println("***Record Updated***");
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}
	}

}
