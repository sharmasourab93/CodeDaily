#Args
def testify(arg1,  *argv):
    print("first argument " + arg1)
    #print(type(argv))
    for arg in argv:
        print("next argument through *argv: " + arg)


testify("hello", "how", "are", "you")


#Kwargs
def hello(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))


hello(game="GeeksforGeeks")
