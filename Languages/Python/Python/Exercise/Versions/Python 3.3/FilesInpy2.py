import os
def make_another_file():
    if os.path.isfile('kanchan.txt'):
        print("You are trying to create a file that already exists")
    else:
        f=open('kanchan.txt',"w")
        f.write("This is how you create a new text file.")
        print("file Created, Text entered and file closed.")
make_another_file()
