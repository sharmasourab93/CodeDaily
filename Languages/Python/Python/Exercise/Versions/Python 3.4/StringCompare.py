#Program to compare strings in a list
class stringcomp:
    "This class gets input from the user"
    "and compares to strings with the user input string"
    def __init__(self):
        self.x1=[]
    def main1(self):
        "Main Function"
        #inputting options for string compare1
        option=int(input("\nWhat do you wish to do?"))
        if(option==1):
            self.addstr()
        elif(option==2):
            self.comparestr()
        elif(option==3):
            print(list(self.x1))
        else:
            exit()
    def addstr(self):
        "Add string to the variable"
        x3=str(input("String\n"))
        x4=self.x1
        x4.append(x3)
    def comparestr(self):
        "User input string compares with the one in list"
        x2=str(input("Enter the string to compare"))
        for i in range (0,len(self.x1),1):
            if(x2==self.x1[i]):
                print("\nString matched at %dth position."%i)
            else:
                print("\nString doesnt match.")
                
    def main(self):
        while(True):
            self.main1()

#Class gets over
String=stringcomp()
String.main()

    
