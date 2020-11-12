# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, -float('inf'))
        
    def dfs(self, root, max_val):
        if not root: 
            return 0  
        res = (root.val >= max_val)
        res += self.dfs(root.left, max(root.val, max_val))
        res += self.dfs(root.right, max(root.val, max_val))
        return res