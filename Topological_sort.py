from Queue import Queue

def toposort(Alist):
#INITIALIZATION
    (indegree, toposortlist) = ({},[])
    zero_degree_q = Queue()
    for i in Alist.keys():
        indegree[i] = 0

#Compute Indegree for each vertex
    for i in Alist.keys():
        for j in Alist[i]:
            indegree[j] = indegree[j] + 1

#Find vertex with Indegree 0 and add it to the queue
    for i in Alist.keys():
        if indegree[i]==0:
            zero_degree_q.push(i)

#Topological Sort Main process
    while (not zero_degree_q.isEmpty()):
        curr_vertex =  zero_degree_q.pop()
        toposortlist.append(curr_vertex)
        indegree[curr_vertex] -= 1
        for adj_vertex in Alist[curr_vertex]:
            indegree[adj_vertex] -= 1
            if indegree[adj_vertex]==0:
                zero_degree_q.push(adj_vertex)

    return (toposortlist, indegree)

AList={0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(toposort(AList))

