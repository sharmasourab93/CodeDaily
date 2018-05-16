#To print doc string at various hierarchies
class funcme:
    "hey this is funcme class"
    def job(self):
        "hey this is a function in a funcme class"
        print(funcme.__doc__)
        print(funcme.job.__doc__)
        print(job.__doc__)
    def main(self):
        print(funcme.job.__doc__)


x=funcme()
x.main()
        

