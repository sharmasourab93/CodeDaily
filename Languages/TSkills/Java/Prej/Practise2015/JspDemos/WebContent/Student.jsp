<%@ page errorPage="Errror.jsp" language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<%
		int sno;
		String name;
		sno=Integer.parseInt(request.getParameter("sno"));
		name=request.getParameter("sname");
		if(sno==1 && name.equals("Tanmay")){
			out.println("Correct Values");
		}else{
			out.println("Invalid Values");
		}
	%>
</body>
</html>