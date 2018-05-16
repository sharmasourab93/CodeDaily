class new_class():
    def __init__(self, number):
        self.multi = int(number) * 2
        self.str = str(number)

a = new_class(2)
print(', '.join(a))
