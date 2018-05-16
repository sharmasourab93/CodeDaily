/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapp;
import java.util.Scanner;
/**
 *
 * @author Sourab Sharma
 */
public class second {
    private int hour;
    private int minute;
    private int second;
    
    public void setTime(int h,int m, int s){
        hour=((h>=0 && h<24)? h : 0);
        minute=((m>=0 && m<60)? m:0);
        second=((s>=0 && s<60)? s:0);
    }
    public String toString(){
        return String.format("%d:%02d:%02d %s", 
                ((hour==0||hour==12)? 12: hour%12),minute,second,((hour<12)? "AM":"PM"));
}
    public second(){
        hour=3;
        minute=6;
        second=36;
    }
    public static void main(String args[]){
        second sec = new second();
        System.out.println(sec.toString());
        sec=new second();
        System.out.println(sec.toString());
    }
        
}
