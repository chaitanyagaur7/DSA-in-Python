from Queue import Queue

def neighbours(Amat,start):
    (rows,cols) = Amat.shape
    nbrs = []
    for j in range(cols):
        if Amat[start,j] == 1:
            nbrs.append(j)
    return nbrs

def BFS(Amat,start):
    visited = {}
    (rows,cols) = Amat.shape
    for each_vertex in range(cols):
        visited[each_vertex] = False
    visited[start] = True
    q = Queue()
    q.push(start)

    while (not q.isEmpty()):
        curr_vertex = q.pop()
        for adj_vertex in neighbours(Amat,curr_vertex):
            if (visited[adj_vertex] == False):
                visited[adj_vertex]=  True
                q.push(adj_vertex)
    return visited

V = [0,1,2,3,4,5,6,7]
E = [(0,1),(0,2),(1,3),(3,5),(2,4),(4,6)]
size = len(V)
import numpy as np
Amat = np.zeros(shape = (size,size))
for (i,j) in E:
    Amat[i,j] = 1
print(BFS(Amat,0))
