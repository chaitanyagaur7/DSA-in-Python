from collections import deque

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

def find_height(root):
    if root is None:
        return 0
    
    height = 0
    q = deque()
    q.append(root)
    while q:
        height += 1
        for i in range(len(q)):
            curr_node = q.popleft()
            if curr_node.left is not None:
                q.append(curr_node.left)
            if curr_node.right is not None:
                q.append(curr_node.right)
    return height 

def check_Balance(root):
    left_height = find_height(root.left)
    right_height = find_height(root.right)

    if abs(left_height-right_height) <= 1:
        return (max(left_height,right_height)) + 1
    else:
        return (-1)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(check_Balance(root))