# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0) # rob, not_rob
            l, r = dfs(node.left), dfs(node.right)
            # rob now:
            rob = node.val + l[1] + r[1]
            # rob later
            # nrob = l[0] + r[0] # this is wrong! not necessary to rob next level as well!
            nrob = max(l) + max(r)
            
            return (rob, nrob)
        
        return max(dfs(root))