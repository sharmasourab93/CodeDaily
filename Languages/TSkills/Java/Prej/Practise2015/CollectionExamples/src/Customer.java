
public class Customer implements Comparable {

	private int custId;
	private String name;
	private int cost;
	
	public Customer() {
		
	}
	
	public Customer(int custId,String name,int cost){
		this.custId=custId;
		this.name=name;
		this.cost=cost;
	}
	
	@Override
	public String toString() {
		return "Cust Id " +getCustId() + " Name " +getName() + " Cost " + getCost();
	}
	
	@Override
	public int compareTo(Object o) {
		Customer c=(Customer)o;
		return getName().compareTo(c.getName());
	}
	
	public int getCustId() {
		return custId;
	}
	public void setCustId(int custId) {
		this.custId = custId;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getCost() {
		return cost;
	}
	public void setCost(int cost) {
		this.cost = cost;
	}
	
}
