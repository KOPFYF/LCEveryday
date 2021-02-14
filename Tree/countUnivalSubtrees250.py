# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, parent):
            # bottom up
            # return True if the subtree (based on current node) is the same as its parent
            if not node: # base, leaf
                return True
            left, right = dfs(node.left, node.val), dfs(node.right, node.val)
            if left and right:
                self.res += 1
            return left and right and node.val == parent
        
        dfs(root, 1001)
        return self.res