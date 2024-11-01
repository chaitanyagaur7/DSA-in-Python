
def rec_Subset(arr, n, index, curr, ans):
    if index >= n:
        ans.append(curr[:])
        return 
    curr.append(arr[index])
    rec_Subset(arr,n,index+1,curr,ans)
    curr.pop()
    rec_Subset(arr,n,index+1,curr,ans) 


arr = [1, 2, 3]
ans = []
curr = []
rec_Subset(arr, len(arr), 0, curr, ans)
print(ans)