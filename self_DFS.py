def DFSInitList(Alist):
    (visited,parent) = ({},{})
    for i in Alist.keys():
        visited[i] = False
        parent = -1
    return(visited,parent)

def DFS(AList, visited,parent,start):
    visited[start] = True

    for adj_vertex in AList[start]:
        if not visited[adj_vertex]:
            parent[adj_vertex] = start
            (visited,parent) = DFSInitList(Amat)
    return (visited,parent)


AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
(v,p)= DFSInitList(AList)
print(DFSList(AList,v,p,0))