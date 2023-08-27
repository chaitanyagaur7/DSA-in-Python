class Queue:
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return (self.queue==[])
    def push(self,v):
        self.queue.append(v)
    def pop(self):
        x = self.queue[0]
        self.queue = self.queue[1:]
        return x
    def display(self):
        print(self.queue)


