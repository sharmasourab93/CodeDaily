x=input("Enter the long string")
list=x.split()
reverseWord=""
for word in list:
    word=word[::-1]
    reverseWord+=word+" "

print(reverseWord)
