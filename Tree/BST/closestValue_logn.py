# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        # O(depth)
        self.res = root.val
        while root:
            if abs(root.val - target) < abs(self.res - target):
                self.res = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return self.res
        
        
        # O(depth)
        self.res = float('inf')
        
        def dfs(node):
            if not node:
                return 
            if target <= node.val:
                dfs(node.left)
            if abs(node.val - target) < abs(self.res - target):
                self.res = node.val
            if target > node.val:
                dfs(node.right)
        
        dfs(root)
        
        return self.res