# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None
        while root:
            if p.val < root.val: # return the first bigger val
                res = root # res could be overwrite multiple times
                root = root.left
            else:
                root = root.right
        return res
        