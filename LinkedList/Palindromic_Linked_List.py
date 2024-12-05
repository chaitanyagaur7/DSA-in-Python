#PALINDROMIC LINKED LIST 

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


#Naive Solution
#Using an external Stack / Array 
#Time Complexity : O(n)
#Space Complexity : O(n)

'''def isPalindrome(head):
        arr = []
        temp = head
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        return arr == arr[::-1]'''

#Optimal Solution 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
        
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

                    