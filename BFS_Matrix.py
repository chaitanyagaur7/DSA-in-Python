from Queue import Queue

def neighbours(Amat,i):
    nbrs = []
    (rows,cols) = Amat.shape
    for j in range(cols):
        if Amat[i,j]==1:
            nbrs.append(j)
    return nbrs

def BFSList(Amat,start):
    (rows,cols) = Amat.shape
    visited = {}
    for each_vertex in range(rows):
        visited[each_vertex] = False

    q = Queue()
    q.push(start)
    visited[start] = True

    while (not q.isEmpty()):
        curr_vertex = q.pop()
        for adj_vertex in neighbours(Amat,curr_vertex):
            if visited[adj_vertex]==False:
                visited[adj_vertex] = True
                q.push(adj_vertex)
    return visited

V = [0,1,2,3,4,5]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
size = len(V)
import numpy as np
AMat = np.zeros(shape=(size,size))
for (i,j) in E:
    AMat[i,j] = 1
print(BFSList(AMat,0))