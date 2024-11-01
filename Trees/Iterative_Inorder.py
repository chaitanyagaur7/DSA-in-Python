class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

def inorder(root):
    stack = []
    res = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        if curr is not None:
            #res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)

            res.append(curr.val)

            if curr.left is not None:
                stack.append(curr.left)
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(inorder(root))