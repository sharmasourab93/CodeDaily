def find_min(arr):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
    return min

def find_max(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max

def find_miss(arr):
    miss=[]
    x=find_min(arr)
    y=find_max(arr)
    for i in range(len(arr)):
        if i==0:
            pass
        elif arr[i]-arr[i-1]>1:
            for j in range(arr[i-1]+1,arr[i]):
                miss.append(j)
    return miss

def find1element(arr):
    sum=0
    for i in arr:
        sum+=i
    rsum=(arr[-1]*(arr[-1]+1))/2
    return rsum-sum
arr=[1,2,4,6,8,10,12]
miss=find_miss(arr)
arr1=[2,3,4,5]
missing=find1element(arr1)
print(miss,missing)