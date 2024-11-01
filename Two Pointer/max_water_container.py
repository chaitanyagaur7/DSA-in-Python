#BRUTE FORCE                   - TC O(n^2)  SC - O(1)
'''def fun(arr):
    area = 0
    curr_area = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            curr_area = min(arr[i],arr[j]) * abs(i-j)
            area = max(curr_area,area)
    return area
'''

#TWO POINTER                 - TC O(n)   SC - O(1)

def fun(arr):
    area = 0
    curr_area = 0
    i,j = 0,len(arr)-1
    while i < j:
        curr_area = min(arr[i],arr[j]) * abs(i-j)
        area = max(curr_area,area)
        if arr[i] < arr[j]:
            i+=1
        else:
            j-=1
    return area 


arr = [1,7,2,5,4,7,3,6]
print(fun(arr))