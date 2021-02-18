# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            # return max depth for current node
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.res = max(self.res, left + right) # no need to -1 because it's count of edges
            return max(left, right) + 1
        dfs(root)
        return self.res