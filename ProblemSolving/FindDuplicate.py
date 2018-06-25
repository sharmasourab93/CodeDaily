#First Duplicate
def naiveapproach(arr):
    stack=[]
    dup=[]
    for i in arr:
        if i in stack and i not in dup:
            dup.append(i)
            print(i)
            #break
        else:
            stack.append(i)
    print(stack,dup)

def optimizedapproach(arr):
    m=max(arr)
    if len(arr)>m:
        m=len(arr)
    new_arr=[0]*m

    for i in range(len(arr)):
        new_arr[arr[i]]+=1
    for i in range(len(new_arr)):
        if new_arr[i]>1:
            print(i)
            #Commenting break will provide all the list of duplicates in optimized way
            break


arr=[1,2,3,6,6,6,7,7,8]
naiveapproach(arr)
optimizedapproach(arr)