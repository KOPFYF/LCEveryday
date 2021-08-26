# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        # post order dfs
        self.res = 0
        def dfs(node):
            # return sum of values of the node's descendants
            if not node:
                return 0
            s = dfs(node.left) + dfs(node.right)
            # print(node.val, s)
            if s == node.val:
                self.res += 1
            return s + node.val
        
        dfs(root)
        return self.res