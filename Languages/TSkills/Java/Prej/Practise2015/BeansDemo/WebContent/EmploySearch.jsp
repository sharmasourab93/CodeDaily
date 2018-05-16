<%@ page import="java.sql.ResultSet" language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<jsp:useBean id="bean1" class="beans.EmploySearch"/>
	<jsp:setProperty  property="*" name="bean1"/>
	<%
		ResultSet rs=bean1.searchEmploy();
		if(rs.next()){
			out.println("Name "+rs.getString("Name")+"<br/>");
			out.println("Department "+rs.getString("Dept")+"<br/>");
			out.println("Designation "+rs.getString("desig")+"<br/>");
			out.println("Basic "+rs.getString("basic")+"<br/>");
		}
		else{
			out.println("Sorry! Record Found.");
		}
	%>
</body>
</html>