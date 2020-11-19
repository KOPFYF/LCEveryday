# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = TreeNode(float('inf'))
        self.min_diff = float('inf')
        self.helper(root)
        return self.min_diff

    def helper(self, root):
        if root:
            self.helper(root.left)
            self.min_diff = min(self.min_diff, abs(self.prev.val - root.val))
            self.prev = root
            self.helper(root.right)