class MyClass:
    def method(self):
        return 'instance method called',self

    @classmethod
    def classmethod(cls):
        return 'cls method called',cls

    @staticmethod
    def statmethod():
        return 'static method called'



m=MyClass()
print(m.method())
print(m.classmethod())
print(MyClass.classmethod(), MyClass.classmethod)
print(MyClass.statmethod(), MyClass.statmethod)
print(m.statmethod(),m.statmethod)
#MyClass.method() #TypeError: method() missing 1 required positional argument: 'self'