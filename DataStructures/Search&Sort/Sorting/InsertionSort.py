#Insertion Sort in Python
def swap(a,b):
    t=a;
    a=b;
    b=a;
def Issort():
    
    #size=int(input("Enter the size of the array"))
    #for n in range(0,size,1):
     #   x[n]=input("\nEnter the element")
    x=[4,3,5,7,9,1,3]
    for i in range(1,len(x),1):
        for k in range(i,1,-1):
            while(k>1 and x[k]<x[k-1]):
                swap(x[k],x[k-1])
    print(x)
    return x
def main():
    print("Welcome to insertion Sort Program")
    Issort()
main()
