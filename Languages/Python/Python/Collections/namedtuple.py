"""
Python: Collections> Namedtuple
								Usage, Function and working of Namedtuple
"""
from collections import namedtuple

# Creating a namedtuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student('Nandini', '19', '2541997')

print("The index used by student's age: {}".format(S[1]))
print("The keyname used by Student's name: {}".format(S.name))
print("Get Student's DOB using getattr(): {}".format(getattr(S, 'DOB')))

# To Convert to an Ordered Dict
di = S._asdict()
print("Dictionary Version of {} is :{}".format(S, di))

# To display all fields
print("To Display all fields {}".format(S._fields))

# To Replace an element fields
print("To replace elements in field {}".format(S._replace(name="Manjeet")))
