import os
def make_file():
    "To make a file"
    #path="D:\\Downloads\\python\\text.txt"
    a=open('text.txt',"w")
    if(a.write!=True):
        try:
            a.write("this way")
            a.close()
        except Exception:
            pass
            #a.open('test.txt',"a")
            #a.write("\n Func that way again")
            #a.close
    
make_file()
