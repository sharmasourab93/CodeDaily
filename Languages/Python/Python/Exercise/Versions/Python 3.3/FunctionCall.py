#program to show that Function calling is what matters in a Python not declaration
def heyyo():
    def hello():
        print("This is Hello")
    print("Heyyo")
    hello()

def main():
    heyyo()

main()

