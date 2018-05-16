#To test  the calling of a function in a class which sounds cumbersome to me
class funcme:
    "hey this is funcme class"
    def hello(self):
        x=int(input("ENter the interger"))
        y=int(input("Enter another integer"))
        self.add(x,y)
    def add(self,a,b):
        z= a+b
        print(z)
    def main(self):
        self.hello()

z=funcme()
z.main()

