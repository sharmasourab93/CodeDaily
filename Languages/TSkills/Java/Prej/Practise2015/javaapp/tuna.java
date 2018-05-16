package javaapp;
public enum tuna {
    bucky("nice","22"),
    kelsey("cutie","10"),
    julia("bigmistake","12");
    private final String desc;
    private final String year;
    tuna(String description, String birthday){
        desc=description;
        year=birthday;
    }
    public String getDesc(){
        return desc;
    }
    public String getyear(){
        return year;
    }
    
}
