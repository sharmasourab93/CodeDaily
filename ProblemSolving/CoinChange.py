def can_give_change(rupee_notes):
    balance=0
    rupee_notes=[i-5 for i in rupee_notes]
    for i in range(len(rupee_notes)):
        balance+=5
        if rupee_notes[i]>balance:
            return i+1
        else:
            pass
    return 0
    print(rupee_notes)
    
    
    

x,y,z=can_give_change([5,10,5,5,5,20]),can_give_change([5,5,5,20]),can_give_change([5,20])
print(x,y,z)
