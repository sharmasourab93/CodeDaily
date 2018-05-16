import java.io.DataOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileOutputStream;

public class DataOutEx {

	/**
	 * @param args
	 */
	public static void main(String[] args){
		// TODO Auto-generated method stub
		try{
			FileOutputStream fout=new FileOutputStream("D:/Sourab Java/data.txt");
		
			DataOutputStream dout=new DataOutputStream(fout);
			dout.writeInt(545);
			dout.writeUTF("Sourab");
			dout.writeDouble(66332.44);
			dout.writeBoolean(true);
			dout.close();
			fout.close();
			System.out.println("Data Saved Successfully");
	}catch(FileNotFoundException e){
		e.printStackTrace();
	}catch(IOException e){
		e.printStackTrace();
		}
	}
}