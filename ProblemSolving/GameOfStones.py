def checkrem(num):
    i=0
    while num>=2:
        if(num>=5): num=num-5
        elif(num>=3): num=num-3
        else:num=num-2
        i+=1
    if num==0:
        if i%2==0:
            return "First"
        else: return "Second"
    elif num==1:
        if i%2==0:
            "First"
        else: return "Second"

def gameofStones(n):
    result=[str]*len(n)
    for i in range(len(n)):
        result[i]=checkrem(arr[i])