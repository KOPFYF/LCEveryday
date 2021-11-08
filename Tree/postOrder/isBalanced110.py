# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # if subtree is balanced, and depth
            if not node:
                return True, 0
            l_bal, l_depth = dfs(node.left)
            r_bal, r_depth = dfs(node.right)
            depth = max(l_depth, r_depth) + 1
            is_bal = l_bal and r_bal and abs(l_depth - r_depth) <= 1
            return is_bal, depth
        
        return dfs(root)[0]