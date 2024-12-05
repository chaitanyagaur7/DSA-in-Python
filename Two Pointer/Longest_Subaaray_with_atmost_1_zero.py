def brute_force(arr):
    max_len = 0
    for i in range(len(arr)):
        curr_zero_count = 0
        curr_len = 0
        for j in range(i,len(arr)):
            if arr[j] == 1:
                curr_len += 1
                max_len = max(curr_len,max_len)
            else:
                curr_zero_count += 1
                if curr_zero_count <= 1:
                    curr_len+=1
                    max_len = max(curr_len,max_len)
                else:
                    
                    break 
    return max_len -1

nums = [0,1,1,1,0,1,1,0,1]
print(brute_force(nums))
nums = [1,1,0,1]
print(brute_force(nums))
nums = [1,1,1]
print(brute_force(nums))



def sliding_window(nums):
        left = 0
        curr_zero_count = 0
        curr_len = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                curr_len += 1
            else:
                curr_zero_count += 1
                while curr_zero_count > 1:
                    if nums[left] == 0:
                        curr_zero_count -= 1
                    left = left + 1
            max_len = max(max_len,right - left + 1 )
        return max_len - 1

nums = [0,1,1,1,0,1,1,0,1]
print(sliding_window(nums))
                
