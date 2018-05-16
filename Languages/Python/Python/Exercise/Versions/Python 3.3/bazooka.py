class Bazooka:
    "This class counts the Number of Bazookas used"
    count=0
    print("Program to Fire Bazooka")
    def _init_(self):
        self.used=used
        Bazooka.count+=1
    def fire(self):
        i=10
        while i>0:
            print(i)
            i-=1
        print("Fire!\n\n\t Bazooka Used")
        Bazooka.count=Bazooka.count+1
    def displaycount(self):
        print("Total Rounds of Bazooka fired: %d"%Bazooka.count)

def main():
    x=Bazooka()
    y=input()
    if (y=="F"):
        x.fire()
        x.displaycount()
        main()
    elif (y!="F"):
        print("Fire Action Terminating...\nTerminated")


main()

