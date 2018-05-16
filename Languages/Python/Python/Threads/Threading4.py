import threading as T
import time
from threading import Thread


def sleeper(i):
    print(i,"in method")
    time.sleep(5)
    print(i,"outside the method")
#print(T.stack_size(64000))
for i in range(5):
    t1=Thread(target=sleeper,args=(i,))
    t2=Thread(target=sleeper,args=(i+5,))
    t1.setName("Thread"+str(i))
    t2.setName("Thread"+str(i+5))
    print(t1.name,t2.name)
    #x=t1.getName()
    t1.start()
    T.Barrier()
    #T.RLock()
    t2.start()
    #print(T.Condition())
    #t1.join()
    #t2.join()