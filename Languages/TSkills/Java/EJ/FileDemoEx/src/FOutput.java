import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
//import java.io.File;
import java.io.IOException;


public class FOutput {
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		try{
			FileInputStream fin=new FileInputStream("D:/Sourab Java/sobby/src/Max3.java");
			FileOutputStream fout=new FileOutputStream("D:/Sourab Java/sobby/src/copy.java");
			int ch;
			while((ch=fin.read())!=-1){
				fout.write((char)ch);
			}
			fin.close();
			fout.close();
			System.out.println("****File Copied****");
			}catch(FileNotFoundException e){
				e.printStackTrace();
			}
		}
}
