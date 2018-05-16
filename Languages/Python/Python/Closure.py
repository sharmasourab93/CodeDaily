def outerFunction(text):
    text=text
    def innerFunction():
        print(text)
    return innerFunction
myFunction=outerFunction('Hey!')
myFunction()
outerFunction('hello')

'''
def logger(func):
    def log_func(*args):
        print(func(*args))
    return log_func
def add(x,y): return x+y
def sub(x,y): return x-y

add_log=logger(add)
sub_log=logger(sub)

add_log(3,3)
sub_log(4,4)
add_log(4,3)
sub_log(4,3)

'''
