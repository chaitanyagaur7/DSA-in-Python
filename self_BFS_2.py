from Queue import Queue

def BFSList(Alist,start):
    visited = {}
    for i in Alist.keys():
        visited[i] = False

    q = Queue()
    visited[start] = True
    q.push(start)

    while (not q.isEmpty()):
        curr_vertex = q.pop()
        for adj_vertex in Alist[curr_vertex]:
            if visited[adj_vertex] == False:
                visited[adj_vertex] = True
                q.push(adj_vertex)
    return visited


AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: [],5: []}
print(BFSList(AList,0))