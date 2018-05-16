import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Custom {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		System.out.println("Enter your name ");
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String name=br.readLine();
		System.out.println("Name is "+name);
	}

}
