package javaapp.intermediate;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import javax.swing.*;
public class gettingitime {
    public static void main(String[] args){
        Calendar calendar = Calendar.getInstance();
        Date date=new Date();
        System.out.println(date);
        SimpleDateFormat sdf = new SimpleDateFormat("dd:MM:YYYY");
        System.out.println(sdf.format(calendar.getTime()));
    }
}

