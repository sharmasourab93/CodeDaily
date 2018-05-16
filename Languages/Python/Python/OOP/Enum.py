import enum
class Animal(enum.Enum):
    dog=1
    cat=2
    lion=3
print("The string representation of enum member is:",end="")
print(Animal.dog)

print("The string representation of enum member is:",end="")
print(repr(Animal.dog))

print("The type of enum member is:",end="")
print(type(Animal.dog))

print("The name of enum member is:",end="")
print(Animal.dog.name)
