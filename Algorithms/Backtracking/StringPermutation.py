#String Permutation
def permuteString(string,l,r):
    if l==r: print(''.join(string))
    else:
        for i in range(l,r+1):
            string[l],string[i]=string[i],string[l]
            permuteString(string,l+1,r)
            string[l], string[i] = string[i], string[l]

string=list("ABC")
permuteString(string,0,len(string)-1)