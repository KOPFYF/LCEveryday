# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.findLeaf(root1) == self.findLeaf(root2)
        
    def findLeaf(self, root: TreeNode) -> list:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.findLeaf(root.left) + self.findLeaf(root.right)