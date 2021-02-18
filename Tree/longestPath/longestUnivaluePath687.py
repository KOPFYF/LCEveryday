# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # O(n) / O(n)
        # reset the left/right to 0 whenever the current node does not match the children node value
        self.res = 0
        def dfs(node):
            # return max depth for current node
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            left = (left + 1) if node.left and node.left.val == node.val else 0
            right = (right + 1) if node.right and node.right.val == node.val else 0
            self.res = max(self.res, left + right) # no need to -1 because it's count of edges
            return max(left, right)
        dfs(root)
        return self.res