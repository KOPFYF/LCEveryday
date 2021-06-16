# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # level by level BFS
        if not root:
            return []
        
        bfs = [root]
        res = [root.val]
        while bfs:
            nxt_bfs = []
            for node in bfs:
                if node.left:
                    nxt_bfs.append(node.left)
                if node.right:
                    nxt_bfs.append(node.right)
            bfs = nxt_bfs
            if bfs:
                res.append(bfs[-1].val)
        return res
                

class Solution2(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def rightview(node, depth):
            if node:
                if depth == len(view):
                    # BFS, when next level, append
                    view.append(node.val)
                # traverse right, then left
                rightview(node.right, depth + 1)
                rightview(node.left, depth + 1)
        view = []
        rightview(root, 0)
        return view