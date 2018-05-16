#Global Scope
def f():
    global s
    print(s)
    s="Me too"
    print(s)
s="I love GeeksForGeeks"
f()

'''
#Another Global Scope
a=1
def f():
    print('Inside f(): %d'%a)
def g():
    a=2
    print('Inside g(): %d'%a)
def h():
    global a
    print('Using Global in h(): %d'%a)
    a=3
    print('Inside h(): %d'%a)
f()
g()
h()
print('Printing a locally/Global: %d'%a)
'''
