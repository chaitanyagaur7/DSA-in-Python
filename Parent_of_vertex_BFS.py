from Queue import Queue

def BFSPathList(AdjList,start):
    visited = {}
    parent = {}

    for i in AdjList.keys():
        visited[i] = False
        parent[i] = -1

    q = Queue()
    visited[start] = True
    q.push(start)

    while (not q.isEmpty()):
        current = q.pop()
        for v in AdjList[current]:
            if (not visited[v]):
                visited[v] = True
                q.push(v)
                parent[v] = current

    return ((visited,parent))


AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(BFSPathList(AList,0))