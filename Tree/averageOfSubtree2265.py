# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node):
            # return (subsum, cnt) of the current subtree
            if not node:
                return 0, 0
            
            lsum, lcnt = dfs(node.left)
            rsum, rcnt = dfs(node.right)
            subsum = lsum + rsum + node.val
            cnt = lcnt + rcnt + 1
            
            if subsum // cnt == node.val:
                self.res += 1
            
            return subsum, cnt
        
        dfs(root)
        
        return self.res