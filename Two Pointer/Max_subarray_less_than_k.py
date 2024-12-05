#Brute force Solution 
'''
def maxSubarray(arr,k):
    curr_sum = 0
    max_len = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i,len(arr)):
            curr_sum = curr_sum + arr[j]
            if curr_sum > k:
                break 
            else:
                max_len = max(max_len,j-i+1)
    return max_len 
'''

#Better Approach


def maxSubarray(arr,k):
    max_len = 0
    i = 0
    j = 1
    curr_sum = arr[j]
    while i < j and j < len(arr):
        curr_sum = curr_sum + arr[j]
        if curr_sum <= k:
            j = j+1
            max_len = max(max_len,j-i)
        else:
            curr_sum = curr_sum - arr[i]
            i = i+1
    return max_len
    
        

arr = input()
k = 14
print(maxSubarray(arr,k))