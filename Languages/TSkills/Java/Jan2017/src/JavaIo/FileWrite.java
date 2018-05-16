/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package JavaIo;
import java.io.IOException;
import java.io.FileWriter;
/**
 *
 * @author esoussh
 */
public class FileWrite {
    public static void main(String[] args) throws IOException{
        //Accept a string 
        String str="File Handling in Java using"+
                "FileWriter and FileReader";
        FileWriter fw=new FileWriter("C:\\Users\\ESOUSSH\\Desktop\\text.txt");
        for(int i=0;i<str.length();i++){
            fw.write(str.charAt(i));
        }
        fw.close();
    }
}
