# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        # for each subtree, (avg, cnt)
        self.res = 0
        def dfs(node):
            if not node:
                return 0.0, 0
            
            lsum, lcnt = dfs(node.left)
            rsum, rcnt = dfs(node.right)
            
            cumsum, cnt = node.val + lsum + rsum, 1 + lcnt + rcnt
            self.res = max(self.res, cumsum / cnt)
            return cumsum, cnt
        
        dfs(root)
        return self.res