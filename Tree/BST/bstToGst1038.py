# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # reverse inorder traversal in descending order
        # Time O(n)
        # Space O(height)
        self.presum = 0
        def inorder(root):
            if root:
                inorder(root.right)
                self.presum += root.val
                root.val = self.presum
                inorder(root.left)
        inorder(root)
        return root