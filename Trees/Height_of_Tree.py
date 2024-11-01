from collections import deque
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

def height(root):
    q = deque()
    q.append(root)
    count = 0
    while q:
        count+=1
        for i in range(len(q)):
            curr = q.popleft()
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
    return count

def height_optimized(root):    #TC -> O(N)  SC -> O(N) in worst case(Skew Tree)
    if root is None:
        return 0
    
    left = height_optimized(root.left)
    right = height_optimized(root.right)
    
    return (1 + max(left,right))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(height(root))
print(height_optimized(root))

