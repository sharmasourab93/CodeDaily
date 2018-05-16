import collections
Student=collections.namedtuple('Student',['name','age','DOB'])
S=Student('Nandini','19','2541997')
print("The student age using index is:",end="")
print(S[1])
#Access using name
print("The student age using keyname is:",end="")
print(S.name)
#Access using getattr()
print("The student DOB using getattr() is: ",end="")
print(getattr(S,'DOB'))
