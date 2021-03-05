# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # delete bottom up
        def dfs(node):
            if not node:
                return 
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val == 0 and not node.left and not node.right:
                node = None
            return node
        
        return dfs(root)