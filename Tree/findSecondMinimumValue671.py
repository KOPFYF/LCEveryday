# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # root node is the smallest node in the tree
        # find a node that is bigger than the root but smaller than any existing node we have come across
        self.res = float('inf')
        self.dfs(root, float('inf'))
        return self.res if self.res != float('inf') else -1
        
    def dfs(self, node, min_val):
        if not node: return 
        
        min_val = min(min_val, node.val)
        
        if min_val < node.val < self.res:
            self.res = node.val
            # Early stopping 
            # if a node value is larger than current second largest, not needs to traverse the branch.
            return 

        self.dfs(node.left, min_val)
        self.dfs(node.right, min_val)