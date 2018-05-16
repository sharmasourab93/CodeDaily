import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
/**
 * Servlet implementation class EmpSearchServlet
 */
@WebServlet("/EmpSearchServlet")
public class EmpSearchServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
    /**
     * @see HttpServlet#HttpServlet()
     */
    public EmpSearchServlet() {
        super();
        // TODO Auto-generated constructor stub
    }
	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		int empno=Integer.parseInt(request.getParameter("empno"));
		try{
			Class.forName("oracle:jdbc.driver.oracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
			PrintWriter out=response.getWriter();
			PreparedStatement pst=con.prepareStatement("select * from Employ where Empn0=?");
			pst.setInt(1,empno);
			ResultSet rs=pst.executeQuery();
			if(rs.next()){
				out.println("Name "+rs.getString("Name")+ "<br/>");
				out.println("Department "+rs.getString("Dept")+"<br/>");
				out.println("Designation"+rs.getString("desig")+"<br/>");
				out.println("Basic "+rs.getString("Basic")+"<br/>");
			}
		}catch(ClassNotFoundException | SQLException e){
			e.printStackTrace();
		}
	}
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}
}