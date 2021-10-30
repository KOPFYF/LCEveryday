# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, depth):
            # return lca, depth
            if not node:
                return node, depth
            lnode, ldepth = dfs(node.left, depth + 1)
            rnode, rdepth = dfs(node.right, depth + 1)
            if ldepth > rdepth:
                return lnode, ldepth
            elif ldepth < rdepth:
                return rnode, rdepth
            else:
                return node, ldepth
        
        return dfs(root, 0)[0]