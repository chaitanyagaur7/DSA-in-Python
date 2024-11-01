from collections import deque
from TreeNode import Treenode
def max_depth(root):
    if root is None:
        return "No Root Found"

    q = deque()
    q.append(root)
    count = 0
    while q:
        count+=1
        for i in range(len(q)):
            curr_node = q.popleft()
            if curr_node.left is not None:
                q.append(curr_node.left)
            if curr_node.right is not None:
                q.append(curr_node.right)
    return count 

root = Treenode(3)
root.left = Treenode(9)
root.right = Treenode(20)
root.right.left = Treenode(15)
root.right.right = Treenode(7)
print(max_depth(root))

    