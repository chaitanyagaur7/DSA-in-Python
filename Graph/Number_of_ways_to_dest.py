from collections import deque 
import heapq

def number_of_ways(Amat,n):
    Alist = {i: [] for i in range(n)}
    for source,dest,time in Amat:
        Alist[source].append((dest,time))
        Alist[dest].append((source,time))
    
    queue = [(0,0)]
    #Initializing Queue with source node (0) that is at cost 0 initially
    min_time = [float('inf')]*(n)
    counter = [0]*(n)
    counter[0] = 1
    while queue:
        curr_node,curr_cost = heapq.heappop(queue)
        if curr_cost > min_time[curr_node]:
            continue
        for adj_node, adj_cost in Alist[curr_node]:
            total_cost = adj_cost + curr_cost
            if total_cost < min_time[adj_node]:
                    min_time[adj_node] = total_cost 
                    heapq.heappush(queue,(adj_node, total_cost))
                    counter[adj_node] = counter[curr_node]
            elif total_cost == min_time[adj_node]:
                    counter[adj_node] += counter[curr_node]
            

    return counter,min_time






n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(number_of_ways(roads, n))  # Output should be the number of ways to reach node 3 with the shortest time.

import heapq

def number_of_ways(Amat, n):
    # Create adjacency list
    Alist = {i: [] for i in range(n)}
    for source, dest, time in Amat:
        Alist[source].append((dest, time))
        Alist[dest].append((source, time))  # Bidirectional graph
    
    # Min-heap for BFS-like traversal (total_cost, current_node)
    queue = []
    heapq.heappush(queue, (0, 0))  # Start at node 0 with cost 0
    
    # Minimum time to reach each node
    min_time = [float('inf')] * n
    min_time[0] = 0
    
    # Counter to track the number of ways to reach each node
    counter = [0] * n
    counter[0] = 1
    
    while queue:
        curr_cost, curr_node = heapq.heappop(queue)
        
        # If the current path's cost is already larger than the minimum known time to this node, skip
        if curr_cost > min_time[curr_node]:
            continue
        
        # Explore adjacent nodes
        for adj_node, adj_cost in Alist[curr_node]:
            total_cost = curr_cost + adj_cost
            
            # If a shorter path is found
            if total_cost < min_time[adj_node]:
                min_time[adj_node] = total_cost
                counter[adj_node] = counter[curr_node]  # Reset counter for new shorter path
                heapq.heappush(queue, (total_cost, adj_node))
            
            # If an equally short path is found
            elif total_cost == min_time[adj_node]:
                counter[adj_node] += counter[curr_node]  # Add number of ways from current node

    # Return the number of ways to reach the destination node (n-1)
    return counter[n-1]

# Example usage
n = 6
roads = [[3,0,4],[0,2,3],[1,2,2],[4,1,3],[2,5,5],[2,3,1],[0,4,1],[2,4,6],[4,3,1]]
print(number_of_ways(roads, n))  # Output should now match the expected value



