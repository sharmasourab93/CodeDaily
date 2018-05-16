/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package JavaIo;
import java.io.FileReader;
import java.io.IOException;
/**
 *
 * @author esoussh
 */
public class FileRead {
    public static void main(String[] args) throws IOException{
        int ch;
        FileReader fr=null;
        fr=new FileReader("C:\\Users\\ESOUSSH\\Desktop\\text.txt");
        while((ch=fr.read())!=-1){
            System.out.print((char)ch);
        }
        fr.close();
    }
  
}
