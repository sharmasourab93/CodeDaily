import java.io.File;
public class FileEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File f1=new File("D:/Sourab Java/sobby/src/Max3.java");
		System.out.println("File Name "+f1.getName());
		System.out.println("Full Name "+f1.getPath());
		System.out.println("Parent Directory "+f1.getParent());
		
		File f2=new File("D:/Java Training/Day1/Examples/src");
		String[] flist=f2.list();
		for(String s:flist){
			System.out.println(s);
		}
	}

}
