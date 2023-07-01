'''PYTHON PROGRAM TO GENERATE THE BFSLIST OF GIVEN ADJACENCY LIST THAT REPRESENT AN UNDIRECTED GRAPH
   The file include a class Queue that was made in order to implement Queue Data Structure in the program and possess the following functions:
   1. isEmpty(): returns True if Queue is Empty, else return False
   2. push():    to append element in the queue
   3. pop():     to return the first element from the queue and remove that from the queue
   4. display(): to display the elementa  
'''

#CODE BY CHAITANYA GAUR 

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

def BFSList(Alist,start):
    visited = {}
    q = Queue()

    for v in Alist.keys():
        visited[v] = False
    visited[start] = True
    q.push(start)
    while (not q.isEmpty()):
        curr_vertex = q.pop()
        for v in Alist[curr_vertex]:
            if not visited[v]:
                visited[v] = True
                q.push(v)
    return (visited)
