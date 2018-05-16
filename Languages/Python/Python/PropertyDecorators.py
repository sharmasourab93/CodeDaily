class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first,last =name.split(' ')
        self.first=first
        self.last=last
emp1=Employee('John','Smith')
print(emp1.fullname)
emp1.fullname='Corey Scahfer'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)
emp1.fullname='Sourab Sharma'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)

