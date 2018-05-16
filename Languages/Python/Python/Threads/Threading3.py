from threading import Thread as t
import time

def sleeper(i):
    print("Thread {} sleeps for 5 second".format(i))
    time.sleep(5)
    print("Thread {} woke up".format(i))

for i in range(20):
    t1=t(target=sleeper,args=(i,))
    t1.start()
    print(t1.name)
    t1.join()
    print(t1.name)

