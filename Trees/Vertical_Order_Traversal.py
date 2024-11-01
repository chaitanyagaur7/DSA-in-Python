from collections import deque
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


d = {}
def vertical_traversal(root,x,y):
    if root is not None:
        vertical_traversal(root.left,x-1,y)
        if x in d.keys():
            d[x].append(root.val)
        else:
            d[x] = [root.val]

        vertical_traversal(root.right,x+1,y)
    return d 

        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(vertical_traversal(root,0,0))