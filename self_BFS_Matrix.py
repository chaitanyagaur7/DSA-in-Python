from Queue import Queue

def neighbores(Amat,i):
    (rows,cols) = Amat.shape
    nbrs = []
    for j in range(cols):
        if Amat[i,j] == 1:
            nbrs.append(j)
    return nbrs

def BFS(Amat,start):
    visited = {}
    (rows,cols) = Amat.shape

    for each_vertex in range(cols):
        visited[each_vertex] = False

    q = Queue()
    visited[start] = True
    q.push(start)

    while (not q.isEmpty()):
        curr_vertex = q.pop()
        for adj_vertex in neighbores(Amat,curr_vertex):
            if visited[adj_vertex]==False:
                visited[adj_vertex]=True
                q.push(adj_vertex)
    return visited

V = [0,1,2,3,4,5]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
size = len(V)
import numpy as np
AMat = np.zeros(shape=(size,size))
for (i,j) in E:
    AMat[i,j] = 1
print(BFS(AMat,0))
