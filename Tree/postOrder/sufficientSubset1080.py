# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, runsum):
            if not node:
                return False
            runsum += node.val
            if not node.left and not node.right:
                return runsum >= limit
            l, r = dfs(node.left, runsum), dfs(node.right, runsum)
            if not l:
                node.left = None
            if not r:
                node.right = None
            return l or r
        res = dfs(root, 0)
        return root if res else None
        
        
        if not root:
            return root
        # case 1: node is leaf
        if not root.left and not root.right:
            if root.val < limit:
                return None # set to None if insufficient
            else:
                return root
        # case 2: node is not leaf
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)
        # all path from this node to leaf is insufficient
        if not root.left and not root.right:
            return None # set to None if insufficient
        else:
            return root