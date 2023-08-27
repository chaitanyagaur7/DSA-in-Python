from Queue import Queue

def BFSList(Alist,start):
    visited = {}
    for i in Alist.keys():
        visited[i] = False
    visited[start] = True
    q = Queue()
    q.push(start)

    while (not q.isEmpty()):
        curr_vertex = q.pop()
        for adj_vertex in Alist[curr_vertex]:
            if not visited[adj_vertex]:
                visited[adj_vertex] = True
                q.push(adj_vertex)
    return visited

def Connected_Components(Alist):
    component = {}
    for i in Alist.keys():
        component[i] = -1

    (compid,seen) = (0,0)  #compid :-> connected component ID     seen:-> number of visited/checked vertices

    while (seen<max(Alist.keys())):
    #FIND THE MINIMUM LEVEL OF VERTICES AMONG ALL THAT IS NOT VISITED
        start_vertex = min([i for i in Alist.keys() if component[i]==-1])
    #CALL THE BFS TO CHECK THE REACHABILITY OF THE VERTEX
        visited = BFSList(Alist,start_vertex)
        for vertex in visited.keys():
            if visited[vertex]:
                seen = seen + 1
                component[vertex] = compid
        compid = compid + 1
    return component
AList = {0: [1], 1: [2], 2: [0], 3: [4, 6], 4: [3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
print(Connected_Components(AList))