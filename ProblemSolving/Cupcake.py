def next_max_calorie(arr):
    while True and len(arr)!=0:
        m=max(arr)
        arr.remove(m)
        yield m

def marcsCakewalk(calorie):
    calorie_arr=calorie
    mile=0
    j=0
    for i in next_max_calorie(calorie_arr):
        mile+=((2**j)*i)
        j+=1
    return mile
