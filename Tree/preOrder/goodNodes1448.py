# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curmax):
            if not node:
                return 0
            res = 0
            if node.val >= curmax: # no nodes with a value greater than X
                res = 1
            else:
                res = 0
            curmax = max(node.val, curmax)
            return res + dfs(node.left, curmax) + dfs(node.right, curmax)
        
        return dfs(root, root.val)
        
        
class Solution1:
    def goodNodes(self, root: TreeNode) -> int:        
        self.res = 0
        def dfs(node, curmax):
            if not node:
                return
            if node.val >= curmax: # no nodes with a value greater than X
                self.res += 1
            curmax = max(node.val, curmax)
            dfs(node.left, curmax)
            dfs(node.right, curmax)
            
        dfs(root, root.val)
        return self.res