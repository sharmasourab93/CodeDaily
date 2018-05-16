filter_me=[1,2,3,4,5,6,7,8,9,10,11,12,13]
result=filter(lambda x: x%3==0, filter_me)
print(*result)
