"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0
        def depth(node):
            # return the max depth of children
            if not node:
                return 0
            max1, max2 = 0, 0
            for child in node.children:
                d = depth(child)
                if d > max1:
                    max1, max2 = d, max1
                elif max1 >= d > max2:
                    max2 = d
                # else: # d <= max2
                #     continue
            self.res = max(self.res, max1 + max2) # no need to -1
            return 1 + max(max1, max2)
        
        depth(root)
        return self.res