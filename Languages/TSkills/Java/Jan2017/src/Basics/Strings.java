package Basics;
import static java.lang.Integer.parseInt;
import java.text.DecimalFormat;
public class Strings {
    String reverse(String string){
        System.out.println("In Reverse Function");
        int y=string.length();
        String rev="";
        for(int i=y;i>0;i--){
            rev+=string.charAt(i);
        }
        System.out.println(rev);
        return rev;
    }
    public void palindrome(String string){
        System.out.println("In Palindrome function");
       Strings x=new Strings();
        String string2=x.reverse(string);
       //string2=this.reverse(string);
       if(string.equals(string2)){
           System.out.println("Reversal of string is :"+string2+" and it a palindrome");
       }else{
           System.out.println("Reversal of string is :"+string2+" and its not a palindrome");
       }
    }
    public void SwapWthird(){
        String a="Hello";
        String b="world!";
        a=a+b;
        b=a.substring(0,a.length()-b.length());
        a=a.substring(b.length());
        String c="Sourab";
        //Returns all characters after the index
        c=c.substring(3);
        System.out.print(a+" "+b+"\n"+c);
    }
  public static void main(String[] args)  {
      String s1="Sourab";
      String s2="Sharma";
      String s3=s1.concat(" ".concat(s2));
      //System.out.println("Value of String S:"+s+"\nLength of String S:"+s.length());
      int x=(s3.lastIndexOf("a"));
      System.out.println(s3+"\nIndex of last a "+x);
      String s4="sourab";
      s4=s4.toUpperCase().toLowerCase();
      Boolean bool=s3.contains(s4);
      System.out.println(s4+" "+bool);
      Strings s=new Strings();
      String s5="Malayalam";
      Boolean bl="Malaya".equalsIgnoreCase("maLaYa");
      System.out.println(bl+" "+s5.replace('y', 'g'));
      try{
          s.palindrome(s5);
      }catch(StringIndexOutOfBoundsException e){
          System.out.println("You have a f***ing error!");
      }      
      int d=1234;
      String obj=new Integer(d).toString();
      //Format which converts integer to string
      DecimalFormat df=new DecimalFormat();
      String obj1=df.format(d);
      int b=parseInt(obj1);
      System.out.println(obj1);
      //Integer can be coverted to string using StringBuffer too 
      //Just add append(integer).toString() to the String buffer variable
      StringBuffer sb=new StringBuffer();
      String obj2=sb.append(d).toString();
      s.SwapWthird();
  }
}
