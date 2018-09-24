"""
Numpy Dimensions are called axes. The No. of axes is called rank
Numpy's dimensions are called axes. The number of axes is rank
Numpy's Array class is called ndarray.
"""
import numpy as np


"""

"""
arr=np.array([[1,2,3],(4,5,6)])
print("Type of the array:",type(arr),type(arr[0]),type(arr[1]))
print("No.of dimensions:", arr.ndim)
print("Shape of the array: ",arr.shape)
print("Size of the array: ", arr.size)
print("Array stores elements of type:",arr.dtype)

np1=np.array([1,2,3,4,5])
np2=np.array([1,2,3,4,5])
np3=np.array([[1,2,4,3],[1,2,3,4]])

print(np1+np2)
print(np1-np2)
print(np1*np2)

print(np1.dtype,np1.shape,np1.size,np3.shape)
np3=np.array([])
np3.copy(np1)
print(np3)