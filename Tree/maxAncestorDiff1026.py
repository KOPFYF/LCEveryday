# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    def maxAncestorDiff(self, root: TreeNode) -> int:
    	# top down
        if not root: return 0
        self.res = 0
        self.dfs2(root, root.val, root.val)
        return self.res 
    
    def dfs2(self, root, minval, maxval):
        if not root: return
        self.res = max(self.res, abs(maxval - root.val), abs(minval - root.val))
        
        minval = min(minval, root.val)
        maxval = max(maxval, root.val)
        self.dfs2(root.left, minval, maxval)
        self.dfs2(root.right, minval, maxval)


class Solution2(object):
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        return self.dfs(root, float('inf'), float('-inf'))
        
    def dfs(self, root, min_val, max_val):
        # return max of diff given current root
        if not root:
            return max_val - min_val
        min_val = min(root.val, min_val)
        max_val = max(root.val, max_val)

        l = self.dfs(root.left, min_val, max_val)
        r = self.dfs(root.right, min_val, max_val)
        return max(l, r)