class MethodOverloading:
    def _init_(self,name):
        self.name=name
        #self.Class=Class
        #self.roll_no=roll_no
        #self.option=option
    def _init_(self,name,Class):
        self.name=name
        self.Class=Class
        #self.roll_no=roll_no
        #self.option=option
    def _init_(self,name,Class,roll_no):
        self.name=name
        self.Class=Class
        self.roll_no=roll_no
        #self.option=option
    def _init_(self,option):
        #self.name=name
        #self.Class=Class
        #self.roll_no=roll_no
        self.option=option
        
    def writefunc(self,name):
        self.name=input("Enter Name")
    def writefunc(self,name,Class):
        self.name=input("Enter Name")
        self.Class=input("Enter Class")
    def writefunc(self,name,Class,roll_no):
        self.name=input("Enter Name")
        self.Class=input("Emter Class")
        self.roll_no=input("Enter Roll_no")
    def opt(self,option):
        if(self.option==1):
            writefunc(self,name)
        elif (self.option==2):
            writefunc(self,name,Class)
        elif (self.option==3):
            writefunc(self,name,Class,roll_no)


y=input("Enter the number of arguments you want in the function")
x=MethodOverloading()
x.opt(y)
