# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # reverse inorder traversal in descending order
        self.suffix_sum = 0
        def helper(root):
            if root:
                helper(root.right)
                root.val += self.suffix_sum
                self.suffix_sum = root.val
                helper(root.left)
        helper(root)
        
        return root