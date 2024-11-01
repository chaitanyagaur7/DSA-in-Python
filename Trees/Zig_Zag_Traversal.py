from collections import deque
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

    def zig_zag_traversal(self):
        if self is None:
            return []
        
        q = deque([self])
        res = []
        level_count = 0
        while q:
            level_size = len(q)
            level_elements = []
   
            for i in range(level_size):
                curr_node = q.popleft()
                level_elements.append(curr_node.val)
                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
            if level_count%2 == 0:
                res.append(level_elements)
            else:
                res.append(level_elements[::-1])
            level_count+=1
        return res
            
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(TreeNode.zig_zag_traversal(root))