# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # DFS, bottom up
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            length = 1 # current node only
            l, r = dfs(node.left), dfs(node.right)
            if node.left and node.left.val == node.val + 1:
                length = max(length, 1 + l)
            if node.right and node.right.val == node.val + 1:
                length = max(length, 1 + r)
            self.res = max(self.res, length)
            return length
        
        dfs(root)
        return self.res