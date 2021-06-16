# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, mx):
            if not node:
                return
            if node.val >= mx:
                self.res += 1
                # print(node.val)
            mx = max(node.val, mx)
            dfs(node.left, mx)
            dfs(node.right, mx)
        
        dfs(root, -10001)
        return self.res
                

class Solution2(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, -10001)
        
    def helper(self, root, ma):

        if not root: 
            return 0
        
        res = (root.val >= ma)
        res += self.helper(root.left, max(root.val, ma))
        res += self.helper(root.right, max(root.val, ma))
        return res