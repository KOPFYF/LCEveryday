# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.current_max = float('-inf') # this must be global
        self.maxPathSumHelper(root)
        return self.current_max

    def maxPathSumHelper(self, root):
        if not root:
            return 0
    
        left = self.maxPathSumHelper(root.left)
        right = self.maxPathSumHelper(root.right)
    
        # like DP, if child is negative, dont take any, just mark as 0
        left = max(left, 0)
        right = max(right, 0)
        
        # current max will be a path passing through the current node, aka left and right in this case
        self.current_max = max(left + right + root.val, self.current_max)
        
        # dfs returns just one biggest child + itself
        return max(left, right) + root.val