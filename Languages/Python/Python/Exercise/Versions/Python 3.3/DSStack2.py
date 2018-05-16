class stack():
    def __init__(self, maxSize=16):
        self.maxSize = maxSize
        self.data = []

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.data) == self.maxSize:
            return True
        else:
            return False

    def push(self, data):
        if not self.isFull():
            self.data.append(data)
            return "OK"
        else:
            return "ERR_Stack_Full"

    def pop(self):
        if not self.isEmpty():
            output = self.data[len(self.data) -1]
            del self.data[len(self.data) -1]
            return output, "OK"
        else:
            return "ERR_Stack_Empty"

    def npop(self, n):
        output = []
        if len(self.data) >= n:
            for i in range(n):
                output.append(self.pop()[0])  
            return output, "OK"
c=stack()
c.push(5)
c.pop()
c.push(10)
