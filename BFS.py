from Queue import Queue

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


AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: [],5:[]}
print(BFSList(AList,0))
