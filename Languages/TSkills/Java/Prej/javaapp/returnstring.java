package javaapp;
public class returnstring {
    private int month;
    private int day;
    private int year;
    public returnstring(int m, int d, int y){
        month=m;
        day=d;
        year=y;
        System.out.printf("This constructor returns string %s\n",this);
    }

    returnstring() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
    public String toString(){
        return String.format("%d Month %d Day %d Year",month,day,year);
    }
}
