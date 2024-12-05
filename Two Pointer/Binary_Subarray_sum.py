def brute_force(arr, k):
    count = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i,len(arr)):
            curr_sum = curr_sum + arr[j]
            if curr_sum == k:
                count+=1
            elif curr_sum > k:
                break 
    return count


def sliding_window(arr,goal):
    count = 0
    left = 0
    curr_sum = 0
    for right in range(len(arr)):
        curr_sum += arr[right]

        while curr_sum > goal and left <= right:
            curr_sum = curr_sum - arr[left]
            left = left + 1
        if curr_sum == goal:
            count+=1
    return count

nums = [1,0,1,0,1]
goal = 2
print(sliding_window(nums, goal))
nums = [0,0,0,0,0]
goal = 0
print(sliding_window(nums,goal))
            
