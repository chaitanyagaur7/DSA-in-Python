V = [0,1,2,3,4,5,6]
E = [(0,1),(1,2),(2,4),(1,3),(4,5),(3,6)]
Adj_List = {}
size = len(V)
for i in range(size):
    Adj_List[i] = []

for (i,j) in E:
    Adj_List[i].append(j)
    Adj_List[j].append(i)
print(Adj_List)