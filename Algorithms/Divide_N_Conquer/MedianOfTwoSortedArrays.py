#Median Of Two Sorted Array
'''
ar1={1,12,15,26,38}
ar2={2,13,17,30,45}

Median after merging data in Sorted Order
{1,2,12,13,15,17,26,30,38,45}
'''


def combine_array(ar1,ar2):
    ar3=list(sorted(ar1+ar2))
    return ar3

def get_median(ar1,ar2,n):
    i=0 #Current index of i/p list ar1[]
    j=0 #current index of i/p list ar2[]
    m1,m2=-1,-1
    """
    Since there are 2n elements, media will be average of elements at index
    n-1 and n in the array obtained after merging ar1 and ar2
    """
    count=0
    while count<n+1:
        count+=1
        
        """
        Below is to handle case where all elements of ar1[] are smaller than smallest
        (or first) element of ar2[]
        """
        if i==n:
            m1,m2=m2,ar2[0]
            break
        elif j==n:
            m1,m2=m2,ar1[0]
            break
        if ar1[i]<ar2[j]:
            m1,m2=m2,ar2[j]
            i+=1
        else:
            m1,m2=m2,ar2[j]
            j+=1
    return sum(m1+m2)/2
        
def find_median(arr):
    if len(arr)%2==0:
        return ((arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)])/2)
    else:
        return arr[int(len(arr)/2)]
ar1=[1,3,5,7]
ar2=[2,4,6,8]
ar3=combine_array(ar1,ar2)
print(ar3,find_median(ar3))