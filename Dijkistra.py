def Dijkistra(Alist,start):
    infinity = float('inf')
    visited = {}
    distance = {}
    for v in Alist.keys():
        visited[v] = False
        distance[v] = infinity
    distance[start] = 0

    for v in Alist.keys():
        min_distance = min([distance[u] for u in Alist.keys() if not visited[u]])
        next_v_list = [u for u in Alist.keys() if not visited[u] and distance[u] == min_distance ]
        next_visited = min(next_v_list)
        visited[next_visited]=True

    for (v,d) in Alist[next_visited]:
        if not visited[v] and distance[next_visited]+d<distance[v]:
            distance[v] = distance[next_visited]+d
    return distance

dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in dedges:
    WL[i].append((j,d))
print(Dijkistra(WL,0))
