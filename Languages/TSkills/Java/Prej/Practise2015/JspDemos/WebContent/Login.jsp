<%@ page import="java.util.*;" language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<%
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
		PreparedStatement pst=con.prepareStatement("select * from users where username=? AND password=?;");
		pst.setString(1,request.getParameter("username").trim());
		pst.setString(2,request.getParameter("password").trim());
		ResultSet rs=pst.executeQuery();
		if(rs.next()){
			%>
			<jsp:forward page="Success.jsp"/>
			<%
		}else{
			%>
			<jsp:forward page="Login.html">
			<% 
		}
	%>
</body>
</html>