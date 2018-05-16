def nextSquare():
    i=1
    while True and i<10:
        yield i*i
        i=i+2

for num in nextSquare():
    if num>100:
        break
    print(num)

'''
def sampleGenerator():

        i=1
        while True:
                yield i*i
                i+=1
        
for i in sampleGenerator():
        print(i)
'''
