import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
/**
 * Servlet implementation class EmployInsertServlet
 */
@WebServlet("/EmployInsertServlet")
public class EmployInsertServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;     
    /**
     * @see HttpServlet#HttpServlet()
     */
    public EmployInsertServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
			PreparedStatement pst=con.prepareStatement("insert into Employ values(?,?,?,?,?)");
			pst.setInt(1,Integer.parseInt(request.getParameter("empno")));
			pst.setString(2, request.getParameter("name"));
			pst.setString(3,request.getParameter("dept"));
			pst.setString(4,request.getParameter("desig"));
			pst.setInt(5,Integer.parseInt(request.getParameter("basic")));
			pst.executeUpdate();
			PrintWriter out=response.getWriter();
			out.println("Record Inserted...");
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}catch(SQLException e){
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
