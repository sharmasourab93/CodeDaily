import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class WriteEmp {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Emp e=new Emp(12,"Kandarp",56733);
		try{
			FileOutputStream fout=new FileOutputStream("D:/Sourab Java/emp.txt");
			ObjectOutputStream objout=new ObjectOutputStream(fout);
			objout.writeObject(e);
			objout.close();
			System.out.println("...Objects Stored Successfully...");
		}catch(FileNotFoundException e1){
			e1.printStackTrace();
		}catch(IOException e1){
			e1.printStackTrace();
		}
	}

}
