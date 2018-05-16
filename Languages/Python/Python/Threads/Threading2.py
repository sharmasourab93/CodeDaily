#Ex1
import time
from threading import Thread as t
def sleeper(i):
    print("Thread {} sleeps for 5 seconds\n".format(i))
    time.sleep(5)
    print("Thread %d woke up\n"%i)

for i in range(10):
    t1=t(target=sleeper,args=(i,))
    t1.start()

#Ex2
'''
import threading

class PrimeNumber(threading.Thread):
    def __init__(self,number):
        threading.Thread.__init__(self)
        self.Number=number

    def run(self):
        counter=2
        while counter*counter<self.Number:
            if self.Number%counter==0:
                print("%d is no prime number, because %d =%d *%d"%(self.Number,self.Number,counter,self.Number/counter))
                return
            
            counter+=1
            print("%d is a prime number"%self.Number)

threads=[]
while True:
    i=int(input("number:"))
    if i<1:
        break
    thread=PrimeNumber(i)
    threads+=[thread]
    thread.start()

for x in threads:
    x.join()
            
'''
