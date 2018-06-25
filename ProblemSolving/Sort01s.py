from collections import Counter as c
'''def sort_arr(arr,size):
    left=0
    right=size
    while left<size/2 and right>size/2:
        if arr[left]==0 and arr[right]==1:
            left+=1
            right-=1
        elif arr[left]!=0 and arr[right]!=1:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        elif arr[left]==0 and arr[right]!=1:
            x=arr[right]
            j=left+1
            while j<size+1:
                arr[j+1]=arr[j]
                j+=1
            arr[left+1]=x
            right-=1
        elif arr[left]!=0 and arr[right]==1:
            x=arr[left]
            j=right-1
            while j>left:
                arr[j]=arr[j-1]
                j-=1
            arr[right-1]=x
            left+=1
    return arr'''
def sort_arr(arr,size):
    left,right=0,size
    while left<right:
        while arr[left]==0 and left<right:
            left+=1
        while arr[right]==1 and left<right:
            right-=1
        if left<right:
            arr[left]=0
            arr[right]=1
            left+=1
            right-=1
    return arr
arr=[0,0,1,0,1,1,1]
count=dict(c(arr))
print(count)
arr=sort_arr(arr,len(arr)-1)

print(arr)