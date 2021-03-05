# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # DFS
        self.res = 0
        left = {} # store the most left node in the dict, key is level, val is left most pos
        def dfs(node, level, pos):
            if node:
                if level not in left:
                    left[level] = pos
                self.res = max(self.res, pos - left[level] + 1)
                dfs(node.left, level + 1, pos * 2)
                dfs(node.right, level + 1, pos * 2 + 1) 
            
        dfs(root, 0, 0)
        return self.res
    
        # BFS
        bfs = [(root, 0)]
        res = 0
        while bfs:
            nxt_bfs = []
            res = max(res, bfs[-1][1] - bfs[0][1] + 1)
            for node, pos in bfs:
                if node.left:
                    nxt_bfs.append((node.left, pos * 2))
                if node.right:
                    nxt_bfs.append((node.right, pos * 2 + 1))
            bfs = nxt_bfs
        return res