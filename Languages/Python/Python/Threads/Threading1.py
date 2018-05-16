import queue
import threading
import urllib.request
'''
def get_url(q,url):
    q.put(urllib.request.urlopen(url))

theurls=["http:google.com","http://yahoo.com"]

q=queue.Queue()

for u in theurls:
    t=threading.Thread(target=get_url,args=(q,u))
    t.daemon=True
    t.start()
s=q.get()
print(s)

'''
import threading
import time
def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    #print('worker')
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(4)
    print(threading.currentThread().getName(), 'Exiting')
t=threading.Thread(name='my_service', target=my_service)
w=threading.Thread(name='worker', target=worker)
w2=threading.Thread(target=worker) #default name
t.start()
w.start()
w2.start()