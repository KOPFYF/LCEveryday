# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0
            lsum, rsum = dfs(node.left), dfs(node.right)
            if node.val == lsum + rsum:
                self.res += 1
            return node.val + lsum + rsum
        
        dfs(root)
        
        return self.res