def DFSInit(Gmat):
    visited = {}
    parent = {}
    for each_Vertex in Gmat.keys():
        visited[each_Vertex] = False
        parent[each_Vertex] = -1

    return (visited,parent)


def FindConnectivitybetweenFriends(v,Gmat, fx, fy):

    Gmat = converttoAdjMat(Gmat)
    (visited,parent) = DFSInit(Gmat)
    visited[v] = True
    l = []
    i = 0
    for curr_vertex in Gmat.keys():
        if visited[curr_vertex]==False:
            parent[curr_vertex] = v
            i = i+1
            (visited,parent) = FindConnectivitybetweenFriends(v,Gmat,fx,fy)

    return (visited,parent)

def converttoAdjMat(Alist):
    adj_dict = {}
    for i in range(len(Alist)):
        adj_dict[i] = []
        for j in range(len(Alist[i])):
            if Alist[i][j] == 1:
                adj_dict[i].append(j)
    return adj_dict

x = [[0,1,1,0,0,0,0],
     [1, 0, 1,1, 1, 1, 0],
     [1,1,0,1,1,1,0],
     [0, 1, 1, 0, 1, 0, 0],
     [0, 1, 1, 1, 0, 1, 0],
     [0, 1, 1, 0, 1, 0, 1],
     [0, 0, 0,0,0,1,0]]
print(converttoAdjMat(x))
vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(FindConnectivitybetweenFriends(vertices, Amat, personX, personY))