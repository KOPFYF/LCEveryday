# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            # return max depth and subtree node
            if not root:
                return 0, None
            (l_depth, l_node), (r_depth, r_node) = dfs(root.left), dfs(root.right)
            if l_depth > r_depth:
                return l_depth + 1, l_node
            elif l_depth < r_depth:
                return r_depth + 1, r_node
            else:
                return l_depth + 1, root
        return dfs(root)[-1]