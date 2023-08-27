class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return (self.stack == [])
    def push(self,v):
        L = []
        L.append(v)
        for i in self.stack:
            L.append(i)
        self.stack = L
        return
    def pop(self):
        x = self.stack[0]
        self.stack = self.stack[1:]
        return x
    def display(self):
        print(self.stack)



