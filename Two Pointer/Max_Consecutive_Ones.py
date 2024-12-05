def brute_force(nums,k):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        count = 0
        curr_k = k
        for j in range(i, len(nums)):
            if nums[j] == 1  and nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            elif nums[j]!=1 and curr_k > 0:
                curr_k -=1
                count+=1
            else:
                break
    return max_count


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(brute_force(nums,k))