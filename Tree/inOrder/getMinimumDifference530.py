# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = TreeNode(float('inf'))
        self.min_diff = float('inf')
        self.helper(root)
        return self.min_diff

    def helper(self, root):
        if root:
            self.helper(root.left)
            self.min_diff = min(self.min_diff, abs(root.val - self.prev.val))
            self.prev = root # this line must updated along with min_diff
            self.helper(root.right)