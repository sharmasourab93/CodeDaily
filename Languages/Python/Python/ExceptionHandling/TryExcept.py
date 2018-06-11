import os
try:
    #If the file does not exist
    #then it would throw an IOError
    file='Sobby.txt'
    f=open(file,'rU')
    text=f.read()
    f.close()

    #control jumps directly to here if
    #any of the above lines throw IOError
except IOError:
    print('Problem reading:'+file)
    
