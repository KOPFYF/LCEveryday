# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursive Traversal with Valid Range
        def dfs(node, low, high):
            if not node:
                return True # empty tree is a valid BST
            if node.val <= low or node.val >= high:
                return False
            return dfs(node.left, low, node.val) \
               and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))
    
        # DFS Iterative Traversal with Valid Range
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
        
        # Recursive Inorder Traversal
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)
    
    
        # O(n) / O(n)
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        for a, b in zip(res, res[1:]):
            if a >= b:
                return False
        return True
            