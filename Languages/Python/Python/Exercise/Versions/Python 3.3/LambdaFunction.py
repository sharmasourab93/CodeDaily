filter_me=[1,2,3,4,5,6,7,8,9,10,11,12]
func=lambda x: x%2==0
result = filter(func, filter_me)
print(*result)
