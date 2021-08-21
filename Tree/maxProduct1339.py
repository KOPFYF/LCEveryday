# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # DFS, O(n) / O(n)
        # one tree with root as root, another subtree rooted at cutoff
        sums, mod = [], 10**9 + 7
        
        def dfs(node):
            if not node:
                return 0
            lsum, rsum = dfs(node.left), dfs(node.right)
            lrsum = lsum + rsum + node.val
            sums.append(lrsum)
            return lrsum
        
        total = dfs(root)
        res = 0
        for s in sums:
            # res = max(res, s * (total - s)) % mod # wont pass
            res = max(res, s * (total - s))
        return res % mod