from Queue import Queue

def BFSPathList(Alist,start):
    visited = {}
    for i in Alist.keys():
        visited[i] = False

    q = Queue()
    visited[start] = True
    q.push(start)

    while (not q.isEmpty()):
        curr_vertex = q.pop()
        for i in Alist[curr_vertex]:
            if not visited[i]:
                visited[i] = True
                q.push(i)
    return visited


def components(Alist):
    component = {}
    for vertex in Alist.keys():
        component[vertex] = -1

    (compid,seen) = (0,0)

    while (seen<max(Alist.keys())):
        startv = min([i for i in Alist.keys() if component[i]==-1])
        visited = BFSPathList(Alist,startv)

        for vertex in visited.keys():
            if visited[vertex]:
                seen = seen + 1
                component[vertex] = compid

        compid = compid+1

    return (component)

AList = {0: [1], 1: [2], 2: [0], 3: [4, 6], 4: [3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
print(components(AList))