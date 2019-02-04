def maximum_cookies(jars):
    max=0
    sum=0
    for i in range(0,len(jars)):
        for j in range(i+2,len(jars),2):
            sum+=jars[j]
        
        if jars[i]+sum>max:
            max=jars[i]+sum
            
    return max
            