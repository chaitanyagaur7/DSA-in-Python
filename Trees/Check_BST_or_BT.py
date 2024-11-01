def check_BST(root):
    if root is None:
        return True 
    if root.left is not None: 
        if root.left.val >= root.val : 
            return False
    if root.right is not None:
        if  root.right.val <= root.val:
            return False

    left = check_BST(root.left)
    right = check_BST(root.right)
    return left and right 

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
print(check_BST(root))