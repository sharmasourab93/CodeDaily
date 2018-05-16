import threading
from threading import Thread

def func1():
    print('Working 1')

def func2():
    print('Working 2')

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
