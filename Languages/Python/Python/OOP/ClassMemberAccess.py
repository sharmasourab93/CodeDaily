class CSStudent:
    stream='cse' #Class Variable
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
a=CSStudent("Geek",1)
b=CSStudent("Nerd",2)

print("Initially")
print("a.stream= " + a.stream)
print(a.name,a.roll)
print("b.stream= " + b.stream)
print(b.name,b.roll,end="\n\n")

CSStudent.stream="Cse"

a.stream="ece" #Changes the particular instance's stream name
print("Later")
print("a.stream= " + a.stream)
print(a.name,a.roll)
print("b.stream= " + b.stream)
print(b.name,b.roll,end="\n\n")

print(CSStudent.stream)

print("\nPost Action ")
CSStudent.stream="mec"  #Changes the class variable 
print("a.stream= " + a.stream)
print(a.name,a.roll)
print("b.stream= " + b.stream)
print(b.name,b.roll)
