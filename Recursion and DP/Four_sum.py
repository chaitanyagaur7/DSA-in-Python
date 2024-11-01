def rec(arr, target, curr, sol, index):
    if len(curr) == 4:
        if target == 0:
            sol.append(curr.copy())
        return 
    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i - 1]:
            continue
        curr.append(arr[i])
        rec(arr,target - arr[i],curr,sol,i+1)
        curr.pop()


arr = [2,2,2,2,2]
target = 0
sol = []
curr = []
rec(arr,target,curr,sol,0)
print(sol)