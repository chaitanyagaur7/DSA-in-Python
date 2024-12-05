#Problem Link : https://leetcode.com/problems/max-consecutive-ones-iii/

#LC - 1004 - MEDIUM 
#Brute Force
'''
def max_Subarrays(arr,k):
    max_len = 0
    for i in range(len(arr)):
        curr_zeroes = 0
        for j in range(i,len(arr)):
            if curr_zeroes > k:
                break 
            else:
                max_len = max(max_len,j-i)
                if arr[j] == 0:
                    curr_zeroes = curr_zeroes + 1
    return max_len
'''

def max_Subarrays(nums,k):
    max_len = 0
    i = 0
    curr_zeroes = 0
    for j in range(len(nums)):
        if nums[j] == 0:
            curr_zeroes += 1

        while curr_zeroes > k:
            if nums[i] == 0:
                curr_zeroes -= 1
            i = i+1
        
        max_len = max(max_len,j-i+1)
    return max_len
        

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(max_Subarrays(nums,k))
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print(max_Subarrays(nums,k))