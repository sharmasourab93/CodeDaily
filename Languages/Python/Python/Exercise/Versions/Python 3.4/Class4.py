#importing another class function into using from and import
from classcallingfun import add
class borrowedclass:
    "borrowed class"
    def blow(self):
        x=int(input())
        y=int(input())
        add(x,y)
    def main(self):
        self.blow()

b=borrowedclass()
b.main()
