# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        bfs = [root]
        res = [[root.val]]
        while bfs:
            nxt_bfs = []
            for cur in bfs:
                if cur.left:
                    nxt_bfs.append(cur.left) 
                if cur.right:
                    nxt_bfs.append(cur.right) 
            bfs = nxt_bfs
            if bfs:
                res.append([v.val for v in bfs])
        return res[::-1]