def matching(b,a):
    if a=='(' and b==')': return True
    if a=='[' and b==']': return True
    if a=='{' and b=='}': return True
    else:return False

def balanced(string):
    stack=[]
    for i in string:
        if i in {'{','[','('}:
            stack.insert(len(stack)-1,i)
        if i in {'}',']',')'}:
            if stack is None:
                return "NO"
            elif not matching(i,stack.pop()):
                return "NO"
    if stack is None:
        return "YES"
    else:
        return "NO"


print(balanced("{}()"))
print(balanced("{]((}"))