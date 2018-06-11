class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('(Initialized School Member: {}'.format(self.name))
    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('(Initialized teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))

t=Teacher("Mrs. ShriVidya",40,30000)
s=Student("Sourab",25,80)

members=[t,s]
for mem in members:
    mem.tell()

