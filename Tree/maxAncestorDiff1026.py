# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root: return 0
        return self.dfs(root, root.val, root.val)
    
    def dfs(self, node, minval, maxval):
        if not node: 
            return maxval - minval
        
        minval = min(minval, node.val)
        maxval = max(maxval, node.val)
        return max(self.dfs(node.left, minval, maxval), self.dfs(node.right, minval, maxval))