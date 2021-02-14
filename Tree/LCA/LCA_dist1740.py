# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        lca = self.LCA(root, p, q)
        d1, d2 = self.dist(lca, p), self.dist(lca, q)
        return d1 + d2
        
    def dist(self, node, target):
        if not node:
            return float('inf')
        if node.val == target:
            return 0
        
        return 1 + min(self.dist(node.left, target), self.dist(node.right, target))
          
    def LCA(self, root, p, q):
        if not root:
            return None
        if root.val in (p, q):
            return root
        l, r = self.LCA(root.left, p, q), self.LCA(root.right, p, q)
        if l and r:
            return root
        if l or r:
            return l or r