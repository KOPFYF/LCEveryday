# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(node):
            if not node.left and not node.right: #leaf node
                if node.val == 1:
                    return True
                else: 
                    return False
                    
            left, right = dfs(node.left), dfs(node.right)
            if node.val == 2: #if node is or
                return left or right
            if node.val == 3: #if node is and
                return left and right
        
        return dfs(root)