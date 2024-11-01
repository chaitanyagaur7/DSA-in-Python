'''Harmonous Array : Suppose karo , ek array hai usme jo bhi current value hai integer ki, to uske aage ke array 
mei utne hi elements exist karnge

Ex : [4,1,2,3,5] -> isme 1st index pe 4 hai, and uske aage 4 aur elements exist karte hai , something like this
'''

''' 
PROBLEM STATEMENT -> Given an array, and tell that kitne elements ko remove karne ke baad wo harmounus banega 

Ex 1: 
i/p -> 
6
[3,4,1,6,7,7]

o/p -> 
1

Explanation -> Removing the first element leads to harmounious seqeuence [4,1,6,7,7] and 
the sequence begins with 4 and has 4 elements 


i/p -> 
5
[1,2,3,4,5]

o/p-> 
2

Explanation -> Longest possible harmonious subsequence is [2,3,4] that can be formed by removing 2 elements 
'''
def isharmonious(arr):
    if len(arr) >= 1 and len(arr) == arr[0]+1:
        return True 
    return False


def harmonious(arr, n, index,count):
    if index >=n:
        return -1
    
    if isharmonious(arr[:index]) or isharmonious(arr[index:]):
        return count 
    
    take_current = harmonious(arr,n,index+1,count+1)

    return take_current

arr1 = [3, 4, 1, 6, 7, 7]
n1 = len(arr1)
print(harmonious(arr1, n1, 0, 0))  # Output should be 1 (removing the first element)

# Input 2
arr2 = [1, 2, 3, 4, 5]
n2 = len(arr2)
print(harmonious(arr2, n2, 0, 0)) 