import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileWriter;
import java.io.FileReader;
public class FileCopy {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File src=new File("D:/Sourab Java/sobby/src/Max3.java");
		File tar=new File("D:/Sourab Java/sobby/src/FileCopy.txt");
		try{
				FileReader fr=new FileReader(src);
				FileWriter fw=new FileWriter(tar);
				
				int ch;
				while((ch=fr.read())!=-1){
					fw.write((char)ch);
				}
				fr.close();
				fw.close();
				System.out.println("***File Copied Successfully***");
			}catch(FileNotFoundException e){
				e.printStackTrace();
		}catch(IOException e){
				e.printStackTrace();
		}
	}

}
