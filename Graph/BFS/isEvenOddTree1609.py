# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # level BFS, O(n)/O(n)
        bfs = deque([root])
        is_even = True
        while bfs:
            prev = None
            for _ in range(len(bfs)):
                node = bfs.popleft()
                if is_even:
                    if node.val % 2 == 0:
                        return False
                    if prev and node.val <= prev.val:
                        return False
                else:
                    if node.val % 2 == 1: 
                        return False
                    if prev and prev.val <= node.val: 
                        return False
                if node.left: 
                    bfs.append(node.left)
                if node.right: 
                    bfs.append(node.right)
                prev = node
            is_even = not is_even # flip
        
        return True    