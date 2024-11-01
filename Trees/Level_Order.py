from collections import deque
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


    def level_order(self):
        if self is None:
            return []
        
        q = deque([self])
        sol = []
        while q:
            curr_size = len(q)
            curr_elements = []
            for i in range(curr_size):
                curr_node = q.popleft()
                curr_elements.append(curr_node.val)

                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
            sol.append(curr_elements)
        return sol


        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(TreeNode.level_order(root))
