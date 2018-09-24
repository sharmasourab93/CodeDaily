import numpy as np
import time,sys
a=np.array([(1,2,3,4),(8,7,6)])
print(a)


# Numpy Vs List
S= range(1000)

print(sys.getsizeof(5)*len(S))

D= np.arange(1000)

print(D.size*D.itemsize)

# Faster than lists

SIZE = 100000

l1=range(SIZE)
l2=range(SIZE)

A1=np.arange(SIZE)
A2=np.arange(SIZE)

start=time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

start=time.time()
result=A1+A2
print((time.time()-start)*1000)

# Operations

a=np.array([(1,2,3,4,5,6,7),(3,2,5,6,1,4,7)])

print(a.ndim,a.itemsize,a.dtype)

print(a.size)
print(a.shape)

a=np.array([(1,2,3,4),(3,4,5,6)])
a=a.reshape(4,2)
print(a)

# Slicing
a=np.array([(1,2,3,4),(3,4,5,6),(7,8,9,10)])
print(a[0,2],a[0:2,3])

a=np.linspace(1,3,5)
print("Linespace",a,type(a))

# Min Max Sum
a= np.array([1,2,3])

print(a.max(),a.min(),a.sum())

# Axis

a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])
print(a.sum(axis=0),a.sum(axis=1))

print(np.sqrt(a),np.std(1))

print(a/b)

#Vertical and Horizantal stakcing
print(np.hstack((a,b)),np.vstack((a,b)))
print(a.ravel())

#log and e

ar=np.array([1,2,3])
print(np.exp(ar))
print(np.log10(ar))























