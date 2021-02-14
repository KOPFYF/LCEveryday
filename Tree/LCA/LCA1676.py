# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Base cases:
# A node can be its own LCA
# However, if left child and right child both return true, 
# the current node becomes the LCA of the left and right subtrees

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def LCA(root):
            if not root: 
                return None
            if root in nodes:
                return root
            l, r = LCA(root.left), LCA(root.right)
            if l and r:
                return root
            if l or r:
                return r or l
        
        return LCA(root)