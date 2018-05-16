package com.java.struts2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;


public class Employ {

	private int empno;
	private String name;
	private String dept;
	private String desig;
	private int basic;
	public int getEmpno() {
		return empno;
	}
	public void setEmpno(int empno) {
		this.empno = empno;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getDept() {
		return dept;
	}
	public void setDept(String dept) {
		this.dept = dept;
	}
	public String getDesig() {
		return desig;
	}
	public void setDesig(String desig) {
		this.desig = desig;
	}
	public int getBasic() {
		return basic;
	}
	public void setBasic(int basic) {
		this.basic = basic;
	}
	
	public String execute() {
		try {

			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","scott","tiger");
			PreparedStatement pst=con.prepareStatement("insert into Employ values(?,?,?,?,?)");
			pst.setInt(1,empno);
			pst.setString(2,name);
			pst.setString(3,dept);
			pst.setString(4,desig);
			pst.setInt(5,basic);
			pst.executeUpdate();
			return "success";
		}
		catch(Exception ex){
			return "failure";
		}
	}
}
