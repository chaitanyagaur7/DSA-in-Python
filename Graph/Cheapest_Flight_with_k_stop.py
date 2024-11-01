'''
PROBLEM - CHEAPEST FLIGHT WITH K STOPS | LC - 787 | MEDIUM |

INTUTION - Use Dijkstra's algorithm by adding an additional condition about no. of stops being less that / equal to k
'''

'''
INPUT FORMAT :
n -> No. of Nodes
k -> Max no. of allowed nodes in a path 
src -> Source node
des -> Destination node
arr[[]] -> 2-D Array as [[source,destination,cost]]
'''
import heapq

'''def cheapest_flight(n,k,src,des,arr):
    #Converting Adjacency Matrix to Adjacency List 
    Alist = {i:[] for i in range(n)}
    for x,y,z in arr:
        Alist[x].append((y,z))
    pq = [(0,src,0)]
    dist = {i: float('inf') for i in Alist.keys()}
    dist[src] = 0
    while pq:
        curr_dist,curr_node,stops = heapq.heappop(pq)

        if curr_node == des:
            return curr_dist
        
        if curr_dist > dist[curr_node] or stops > k:
            continue 
        
        for adj_node, adj_dist in Alist[curr_node]:
            distance = adj_dist + curr_dist
            if k >= stops and  distance < dist[adj_node]:
                dist[adj_node] = distance 
                heapq.heappush(pq,(distance, adj_node, stops+1))
    return -1'''
from collections import deque

def cheapest_flight(n,k,src,des,flight):
    Alist = {i:[] for i in range(n)}
    for i in flight:
        Alist[i[0]].append((flight[1],flight[2]))

    queue = deque((0,src,0))
    cost = {i:float('inf') for i in Alist.keys()}

    cost[src] = 0

    while queue:
        (curr_cost,curr_node,curr_stops) = queue.popleft()

        if curr_node == des:
            return curr_cost 
        
        if k < curr_stops:
            continue 

        for adj_node,adj_cost in Alist[curr_node]:

            distance = adj_cost + curr_cost
            if k >= curr_stops and  distance < cost[adj_node]:
                    cost[adj_node] = distance 
                    queue.append((adj_cost,adj_node))
        return -1

# Example usage:
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]] 
src = 0
dst = 2
k = 1

# Find the cheapest flight with at most k stops
result = cheapest_flight(n, k, src, dst, flights)
print(result)  # Output: 300 (0 -> 1 -> 2 -> 3 with cost 100+100+100)
















