#Data Hiding
class MyClass:
    #Hidden with __
    __hidden=0
    def add(self,increment):
        self.__hidden+=increment
        print(self.__hidden)
m=MyClass()
m.add(2)
m.add(10)
# To print the hidden members of the class
print(m._MyClass__hidden)
