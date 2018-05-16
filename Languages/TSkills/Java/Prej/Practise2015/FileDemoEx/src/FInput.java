import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class FInput {

	public static void main(String[] args) throws FileNotFoundException {
		// TODO Auto-generated method stub
		try {
			FileInputStream fin=new FileInputStream("D:/Sourab Java/sobby/src/Max3.java");
			int ch;
			while((ch=fin.read())!=-1){
				System.out.println((char)ch);
			}
			fin.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
