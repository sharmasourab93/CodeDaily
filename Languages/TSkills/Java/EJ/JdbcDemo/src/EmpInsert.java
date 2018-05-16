import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;

public class EmpInsert {
	public static void main(String[] args) throws SQLException {
		// TODO Auto-generated method stub
		int empno, basic;
		String name,dept,desig;
		System.out.println("Enter Employ No,Name, Dept, Desig and Basic:");
		Scanner scan=new Scanner(System.in);
		empno=Integer.parseInt(scan.nextLine());
		name=scan.nextLine();
		dept=scan.nextLine();
		desig=scan.nextLine();
		basic=Integer.parseInt(scan.nextLine());
		try{
				Class.forName("oracle.jdbc.driver.OracleDriver");
				Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
				PreparedStatement pst=con.prepareStatement("insert into Employ values(?,?,?,?,?)");
				pst.setInt(1, empno);
				pst.setString(2, name);
				pst.setString(3, dept);
				pst.setString(4, desig);
				pst.setInt(5,basic);
				pst.executeUpdate();
				System.out.println("Record Inserted");
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}
	}

}
