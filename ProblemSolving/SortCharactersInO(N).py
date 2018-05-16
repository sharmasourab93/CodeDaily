def sort_in_N(arr):
    char_arr=[0]*26
    for i in range(len(arr)):
        char_arr[ord(arr[i])-ord('a')]+=1
    for j in range(26):
        if char_arr[j]!=0:
            print(chr(ord('a')+j)*char_arr[j],end="")

arr="geeksforgeeks"
sort_in_N(arr)


