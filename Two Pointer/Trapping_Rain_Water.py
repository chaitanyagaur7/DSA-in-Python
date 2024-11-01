def trap_rain(arr):                           # TC -> O(n)   SC -> O(n)
    left = [0] * len(arr)
    right = [0] * len(arr)
    ans = 0
    max_left,max_right = 0,0
    for i in range(len(arr)):
        if arr[i] > max_left:
            max_left = arr[i]
        left[i] = max_left
    for j in range(len(arr)-1,-1,-1):
        if arr[j] > max_right:
            max_right = arr[j]
        right[j] = max_right
    for i in range(len(arr)):
        ans += (min(left[i],right[i]) - arr[i])
    return ans

arr = [4,2,0,3,2,5]
print(trap_rain(arr))
    



            