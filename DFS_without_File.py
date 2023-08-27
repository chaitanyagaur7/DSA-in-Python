#DFS WITHOUT STACK


#INITIALISATION FUNCTION
def DFSinitList(Alist):
    visited = {}
    parent = {}
    for each_vertex in Alist.keys():
        visited[each_vertex] = False
        parent[each_vertex] = -1
    return (visited,parent)


#MAIN FUNCTION
def DFS(Alist,visited,parent,v):
    visited[v] = True

    for adj_vertex in Alist[v]:
        if not visited[adj_vertex]:
            parent[adj_vertex] = v

            (visited,parent) = DFS(Alist,visited,parent,adj_vertex)

    return (visited,parent)

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
v,p = DFSinitList(AList)
print(DFS(AList,v,p,0))