#Problem Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/

#LC - 3 - MEDIUM 

#BRUTE FORCE METHOD 
'''def longest_substring(s : str) -> str:

    max_len = 0
    for i in range(len(s)):
        visited = set()
        for j in range(i,len(s)):
            if s[j] not in visited:
                visited.add(s[j])
                max_len = max(max_len,j-i+1)
            else:
                break
    return max_len 
'''
# BETTER APPROACH 

'''def longest_substring(s : str) ->str:
    visited = []
    i = 0
    j = 1
    max_len = 0
    while j < len(s) and i<j:
        if s[j] not in visited:
            visited.append(s[j])
            max_len = max(max_len,j-i)
            j = j+1
        else:
            i = i+1
            visited = visited[i:]
    return max_len'''








#REVISION APPROACH - Brute Force - Time - 5 Minutes
def longest_substring(s):
    max_len = 0
    for i in range(len(s)):
        visited = set()
        curr_count = 0
        for j in range(i,len(s)):
            if s[j] in visited:
                visited = set()
                break 
            else:
                visited.add(s[j])
                curr_count+=1
        if curr_count > max_len:
            max_len = curr_count 
    return max_len


s = 'pwwkew'
print(longest_substring(s))

#Revision Approach - Sliding Window - Time Taken - 10 Minutes

def longest_substring(s):
    left = 0
    max_len = 0
    visited = set()
    for right in range(left,len(s)):
        while s[right] in visited:
            visited.remove(s[left])
            left += 1
        visited.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


s = 'pwwkew'
print(longest_substring(s))














            

