#Divide & Conquer Algorithm
#O(n)
def power(x,y):
    if y==0: return 1
    elif ((int(y%2))==0):
        return (power(x,int(y/2)))*(power(x,int(y/2)))
    else:
        return x*power(x,int(y/2))*power(x,int(y/2))

#O(log n)
def optimized_power(x,y):
    if y==0: return 1
    temp=optimized_power(x,y/2)
    if y%2==0: return temp*temp
    else: return x*temp*temp
x=3
y=3
print("Naive: ",power(x,y))
print("Optimized: ",power(x,y))