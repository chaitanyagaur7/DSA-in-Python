class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
    
def max_path_sum(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val
    left_sum =max_path_sum(root.left)
    right_sum = max_path_sum(root.right)
    return root.val + max(left_sum,right_sum)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
'''root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)'''
print(max_path_sum(root))