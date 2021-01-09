# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # level by level BFS
        if not root:
            return []
        bfs = [root]
        ans = []
        while bfs:
            ans.append(max(node.val for node in bfs))
            nxt_level = []
            for node in bfs:
                # for loop is the key to loop level by level
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
            bfs = nxt_level
        return ans