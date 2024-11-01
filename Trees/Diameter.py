#Diameter of a binaru tree is length of maximum nodes at each nodes left + right (including or excluding root)
from collections import deque
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
def diam(root,max_diam):
    if root is None:
        return 0
    
    left = diam(root.left,max_diam)
    right = diam(root.right,max_diam)
    max_diam[0] = max(max_diam[0],left+right)
    return (1 + max(left,right))



#TIME COMPLEXITY : O(n^2)              SPACE COMPLEXITY : O(n) (Because we are using a Queue data structure)
def height(root):
    if root is None:
        return 0
    
    left = height(root.left)
    right = height(root.right)
    return (1 + max(left,right))

def diameter(root):
    if root is None:
        return 0
    
    max_diam = 0
    q = deque()
    q.append(root)
    while q:
        for i in range(len(q)):
            curr_node = q.popleft()
            if curr_node.left is not None and curr_node.right is not None:
                if height(curr_node.left) + height(curr_node.right) > max_diam:
                    max_diam = height(curr_node.left) + height(curr_node.right)
                q.append(curr_node.left)
                q.append(curr_node.right)
            elif curr_node.left is not None:
                if height(curr_node.left) > max_diam:
                    max_diam = height(curr_node.left)
                q.append(curr_node.left)
            elif curr_node.right is not None:
                if height(curr_node.right) > max_diam:
                    max_diam = height(curr_node.right)
                q.append(curr_node.right)
    return max_diam



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(diameter(root))
max_diam = [0]
diam(root,max_diam)
print(max_diam[0])