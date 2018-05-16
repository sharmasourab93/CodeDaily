import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.sql.Date;
public class ObjectinEx {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			FileInputStream fin=new FileInputStream("D:/objext.txt");
			ObjectInputStream objin=new ObjectInputStream(fin);
			String s=(String)objin.readObject();
			Date dt=(Date)objin.readObject();
			System.out.println(s+dt);
			objin.close();
			fin.close();
			
		}catch(FileNotFoundException e){
			e.printStackTrace();
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}
