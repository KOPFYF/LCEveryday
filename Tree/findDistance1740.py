# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def LCA(root, p, q):
            if not root: return
            if p == root.val or q == root.val:
                return root
            
            l, r = LCA(root.left, p, q), LCA(root.right, p, q)
            if l and r: 
                return root
            if l or r:
                return r or l
        
        def dist(node, target):
            if not node: 
                return float('inf')
            if node.val == target:
                return 0
            return 1 + min(dist(node.left, target), dist(node.right, target))
        
        lca = LCA(root, p, q)
        return dist(lca, p) + dist(lca, q)
        