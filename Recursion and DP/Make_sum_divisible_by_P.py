def rec(arr, index, p, curr):
    if p == 0:
        return curr[:]  
    if p < 0 or index == len(arr):
        return None  

    curr.append(arr[index])
    take = rec(arr, index + 1, p - arr[index], curr)
    curr.pop()  

    not_take = rec(arr, index + 1, p, curr)

    return take if take is not None else not_take

ar = [3,1,4,2]
p = 9
print(rec(ar,0,p,[]))