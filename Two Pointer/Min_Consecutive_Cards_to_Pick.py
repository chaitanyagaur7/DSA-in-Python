
#Problem Link : https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

#LC - 2260 - MEDIUM 

#BRUTE FORCE - 7 Min

def min_cards(arr):
    min_len = float('inf')
    for i in range(len(arr)):
        visited = set()
        for j in range(i,len(arr)):
            if arr[j] in visited:
                min_len = min(min_len, j - i + 1)
                break
            else:
                visited.add(arr[j])
    if min_len != float('inf'):
        return min_len 
    return -1

cards = [3,4,2,3,4,7]
print(min_cards(cards))
cards = [1,0,5,3]
print(min_cards(cards))

#Optimized Solution 


def min_card(cards):
        left = 0
        min_len = float('inf')
        visited = set()
        for right in range(left,len(cards)):
            if cards[right] in visited:
                min_len = min(min_len,right - left + 1)
                left+=1
                visited.remove(cards[left])
            visited.add(cards[right])
        return min_len if min_len != float('inf') else -1

        

cards = [95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]

print(min_cards(cards))
cards = [1,0,5,3]
print(min_cards(cards))
