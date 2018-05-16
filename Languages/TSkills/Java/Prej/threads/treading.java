package threads;
import java.util.*;
//Runnable implements Run!!
public class treading implements Runnable{
    String name;
    int time;
    Random r=new Random();
    
    public treading(String x){
        name=x;
        time=r.nextInt(999);
        
    }
    public void run(){
        try{
            System.out.printf("%s is  sleeping for %d\n",name,time);
            Thread.sleep(time);
            System.out.printf("\n%s is done",name);
        }catch(Exception e){
            System.out.println("Hell Yeah! Its an error!");
        }
    }
}
