# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':       
        self.flagp = False
        self.flagq = False
        res = self.helper(root, p, q)
        if not self.flagp or not self.flagq: 
            return None
        return res
        
    def helper(self, root, p, q):
        if not root:
            return None
        left, right = self.helper(root.left, p, q), self.helper(root.right, p, q)
        if root == p:
            self.flagp = True
            return root
        if root == q:
            self.flagq = True
            return root 
        if left and right:
            return root
        if left or right:
            return right or left