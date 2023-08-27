from Stack import Stack

def DFSPathList(Alist,start):
    visited = {}
    for i in Alist.keys():
        visited[i] = False

    visited[start] = True
    st = Stack()
    st.push(start)

    while (not st.isEmpty()):
        curr_vertex = st.pop()
        if visited[curr_vertex]==False:
            visited[curr_vertex] = True
        for adj_vertex in Alist[curr_vertex]:
            if (not visited[adj_vertex]):
                st.push(adj_vertex)
    return (visited)


AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(DFSPathList(AList,0))