import sys
b=["Namo","Jordan","Bama","Philipose","Vladimir","Makarov","Sandipan"]
for a in range(0,10,1):
    try:
        if a<7:
            print("The Name in the first list is:%s"%b[a])

    except (KeyError,TypeError) as error:
        print("Leaders Not found")
    except (TypeError):
        pass
y=input("Do you want to Add any leaders to the list?")
if (y=="Yes" or y=="yes"):
    l=input("Enter the New Leader")
    k=b.append(l)
    print(k)

else:
    print("Thank You for taking Interest")
    
