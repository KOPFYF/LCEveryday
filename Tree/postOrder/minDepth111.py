# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1 # base case leaf
            # path has to be valid
            # if I dont check child, it will return 0 in invalid path
            min_depth = float('inf')
            if node.left:
                min_depth = min(min_depth, depth(node.left))
            if node.right:
                min_depth = min(min_depth, depth(node.right))

            return min_depth + 1
        
        return depth(root)