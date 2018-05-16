import sys
import os
def make_text_file():
    a=open('test.txt',w)
    a.write("This is how you create a new text file")
    a.close()

make_text_file()
