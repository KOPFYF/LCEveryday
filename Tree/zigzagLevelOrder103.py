# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS
        if not root: return []
        res = [[root.val]]
        bfs = [root]
        
        level = 0
        while bfs:
            level += 1
            nxt_bfs = []
            for cur in bfs:
                if cur.left:
                    nxt_bfs.append(cur.left)
                if cur.right:
                    nxt_bfs.append(cur.right)
            bfs = nxt_bfs
            if nxt_bfs:
                tmp = [node.val for node in nxt_bfs]
                res.append(tmp[::-1] if level % 2 else tmp)
        return res