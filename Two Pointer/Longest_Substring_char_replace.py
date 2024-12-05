def brute_force(s,k):
    arr = [0]*26
    max_arr = 0
    changes = 0
    for i in range(len(s)):
        curr_changes = 0
        for j in range(i,len(s)):
            print(ord(s[j])," ",ord('A'))
            arr[ord(s[j]) - ord('A')] += 1
            curr_changes = (j - i + 1) - max(arr)
            if curr_changes <= k:
                max_arr = max(max_arr, j-i+1)
    return max_arr
            


def sliding_window(s,k):
    arr = [0]*26
    left = 0
    max_arr = 0
    for right in range(len(s)):
        arr[ord(s[right]) - ord('A')] += 1
        curr_changes = (right - left + 1) - max(arr)
        while curr_changes > k:
            arr[ord(s[left]) - ord('A')] -= 1
            if arr[ord(s[left])] != max(arr):
                curr_changes -= 1
            left = left + 1
        max_arr = max(max_arr, right - left +1)
    return max_arr


s = "AABABBA"
k = 1
print(sliding_window(s,k))

