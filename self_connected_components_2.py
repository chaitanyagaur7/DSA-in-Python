from Queue import Queue

def BFSList(Alist,start):
    visited = {}
    for i in Alist.keys():
        visited[i] = False

    q = Queue()
    q.push(start)
    visited[start] = True

    while (not q.isEmpty()):
        curr_vertex = q.pop()
        for adj_vertex in Alist[curr_vertex]:
            if not visited[adj_vertex]:
                visited[adj_vertex] = True
                q.push(adj_vertex)
    return visited

def Connected_Components(Alist):
    components = {}
    for i in Alist.keys():
        components[i] = -1

    (seen, compid) = (0,0)

    while (seen < max(Alist.keys())):
        start_vertex = min([i for i in Alist.keys() if components[i]==-1])
        visited = BFSList(Alist,start_vertex)

        for vertex in visited.keys():
            if visited[vertex]:
                seen+=1
                components[vertex] = compid

        compid+=1
    return components

AList = {0: [1], 1: [2], 2: [0], 3: [4, 6], 4: [3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
print(Connected_Components(AList))