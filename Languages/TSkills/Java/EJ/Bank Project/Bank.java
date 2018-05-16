import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


public class Bank {
	private int accountNo;
	private String Firstname;
	private String lastname;
	private String city;
	private String state;
	private int amount;
	private String cheqFacil;
	private String accountType;
	
	Connection con;
	PreparedStatement pst;
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	public int getAmount() {
		return amount;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	public String getAccountType() {
		return accountType;
	}

	public void setAccountType(String accountType) {
		this.accountType = accountType;
	}

	public String getCheqFacil() {
		return cheqFacil;
	}

	public void setCheqFacil(String cheqFacil) {
		this.cheqFacil = cheqFacil;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getLastname() {
		return lastname;
	}

	public void setLastname(String lastname) {
		this.lastname = lastname;
	}

	public String getFirstname() {
		return Firstname;
	}

	public void setFirstname(String firstname) {
		Firstname = firstname;
	}

	public int getAccountNo() {
		return accountNo;
	}

	public void setAccountNo(int accountNo) {
		this.accountNo = accountNo;
	}
	public int generateAccountNo(){
		con=DaoConnection.getConnection();
		try{
				pst=con.prepareStatement("select Max(AccountNo) from Accounts");
				ResultSet rs=pst.executeQuery();
				if(rs.next()){
						int accno=rs.getInt("Accno");
						accno++;
						return accno;
				}else{
					return 1;
				}
		}catch(SQLException e){
			e.printStackTrace();
		}
		return 0;
	}
}
