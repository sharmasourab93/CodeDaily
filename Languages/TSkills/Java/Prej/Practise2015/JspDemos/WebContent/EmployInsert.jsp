<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
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
	PreparedStatement pst=con.prepareStatement("insert into Employ values(?,?,?,?,?)");
	pst.setInt(1,Integer.parseInt(request.getparameter("empno")));
	pst.setString(2,request.getParameter("name"));
	pst.setString(3,request.getParameter("dept"));
	pst.setString(4,request.getParameter("desig"));
	pst.setInt(5,Integer.parseInt(request.getParameter("basic")));
	pst.executeUpdate();
	out.println("Record inserted...");
	%>
</body>
</html>