import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class ScanFile {

	public static void main(String[] args) {
		try {
			FileWriter fw=new FileWriter("d:/data.txt");
			fw.write("12 5 hello true hi 4.3 23 56 3.4 bye 5 23.3 66");
			fw.close();
			FileInputStream fin=new FileInputStream("d:/data.txt");
			Scanner scr=new Scanner(fin);
			
			while(scr.hasNext()){
				if(scr.hasNextBigInteger()){
					int x=scr.nextInt();
					System.out.println(x);
				}
				else {
					scr.next();
				}
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
