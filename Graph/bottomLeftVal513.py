# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        bfs = [root]
        while bfs:
            # since lastly bfs must be empty list, we update ans firstly
            ans = bfs[0].val
            nxt = []
            for node in bfs:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            bfs = nxt
        return ans