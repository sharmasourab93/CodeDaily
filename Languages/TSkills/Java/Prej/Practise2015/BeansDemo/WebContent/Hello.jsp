<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<jsp:useBean id="bean1" class="beans.HelloWorld"/>
	Default Value:
	<b>
		<jsp:getProperty property="greeting" name="bean1"/>
		</b><br/><br/>
		<jsp:setProperty property="greeting" name="bean1" value="good evening"/>
		Update Value:
		<jsp:getProperty property="greeting" name="bean1"/>
</body>
</html>