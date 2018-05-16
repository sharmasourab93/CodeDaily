arr=[1,2,3,4]
tup=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        tup.append((arr[i],arr[j]))
for i in range(len(tup)):
    tup[i]=abs(tup[i][0]-tup[i][1])
print(tup,min(tup))
