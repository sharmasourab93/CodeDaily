#Input  Dogs like cats
#Output Cats like dogs
string="Dogs barking like purring cats"

x=string.split(' ')
print(x)
n=len(x)-1
for i in range(0,(n//2)):
    x[i],x[n-i]=x[n-i],x[i]

print(' '.join(x))

print(string[0].upper())