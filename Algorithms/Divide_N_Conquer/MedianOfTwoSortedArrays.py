#Median Of Two Sorted Array
'''
ar1={1,12,15,26,38}
ar2={2,13,17,30,45}

Median after merging data in Sorted Order
'''


def combine_array(ar1,ar2):
    ar3=list(sorted(ar1+ar2))
    return ar3

def find_median(arr):
    if len(arr)%2==0:
        return ((arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)])/2)
    else:
        return arr[int(len(arr)/2)]
ar1=[1,3,5,7]
ar2=[2,4,6,8]
ar3=combine_array(ar1,ar2)
print(ar3,find_median(ar3))