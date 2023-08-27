def MinOrderDish(L):
    orderDict = {}
    orderList = [1001,1002,1003,1004,1005,1006,1007,1008,1009]
    L = []
    for i in orderList:
        orderDict[i] = 0
    for i in L:
        orderDict[i] = orderDict[i]+1
    for i in orderDict.keys():
        x = orderDict.get(1001)
        for i in orderDict.keys():
            if i.value()>x:
                x = i.value()

        L.append(x)
        print(L)



    return orderDict


L = [1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]
print(MinOrderDish(L))