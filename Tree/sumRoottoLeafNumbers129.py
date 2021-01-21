# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # DFS to find path
        if not root:
            return 0
        paths = []
        def dfs(node, path):
            if not node.left and not node.right: # leaf
                paths.append(path + [node.val])
            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path + [node.val])
        dfs(root, [])
        # print(paths)

        res = 0
        for path in paths:
            n = len(path)
            for i in range(n):
                res += path[i] * (10 ** (n - i - 1))
        return res