import heapq

def dijkstras(Alist,start):
    distance = {}
    for i in Alist.keys():
        distance[i] = float('inf')
    distance[start] = 0
    queue = [(0,start)]

    while queue:
        curr_dist,curr_node = heapq.heappop(queue)
        if curr_dist > distance[curr_node]:
            continue 

        for adj_node, adj_distance in Alist[curr_node].items():
            curr_distance = adj_distance + curr_dist

            if curr_distance < distance[adj_node]:
                distance[adj_node] = curr_distance
                heapq.heappush(queue,(curr_distance, adj_node))
    return distance 

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstras(graph, start_node)

print(distances)
