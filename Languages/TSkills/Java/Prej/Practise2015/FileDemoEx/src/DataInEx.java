import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
public class DataInEx {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			FileInputStream fin=new FileInputStream("D:/Sourab Java/sob.txt");
			DataInputStream din=new DataInputStream(fin);
			int x=din.readInt();
			String name=din.readUTF();
			double y=din.readDouble();
			boolean flag=din.readBoolean();
			System.out.println("X value is "+x);
			System.out.println("Name is "+name);
			System.out.println("Double Value "+y);
			System.out.println("Flag Value "+flag);
			din.close();
			fin.close();
		}catch(FileNotFoundException e){
			e.printStackTrace();
		}catch(IOException e){
			e.printStackTrace();
		}
	}	
}
