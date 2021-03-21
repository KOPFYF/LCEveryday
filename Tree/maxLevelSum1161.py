# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:  
        bfs = [root]
        level, max_l, max_s = 0, 0, -float('inf')

        while bfs:
            s = 0
            level += 1
            nxt_bfs = []
            for cur in bfs:
                s += cur.val
                if cur.left:
                    nxt_bfs.append(cur.left)
                if cur.right:
                    nxt_bfs.append(cur.right)
            if s > max_s:
                max_l = level
                max_s = s
            bfs = nxt_bfs
        return max_l