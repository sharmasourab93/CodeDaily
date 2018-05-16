import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.Serializable;


public class ReadEmp implements Serializable{

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			FileInputStream fin=new FileInputStream("D:/Emp.txt");
			ObjectInputStream objin=new ObjectInputStream(fin);
			Emp e=(Emp)objin.readObject();
			System.out.println(e);
		}catch(FileNotFoundException e){
			e.printStackTrace();
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}catch(IOException e){
			e.printStackTrace();
		}

	}

}
