# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # compare the current node and its previous node in the "in order traversal"
        # iteratively
        pre = first = second = None
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if not first and pre and pre.val > node.val:
                first = pre
            if first and pre and pre.val > node.val:
                second = node
            pre = node
            root = node.right
        first.val, second.val = second.val, first.val
        
        # recursively
        first, second, pre = None, None, TreeNode(float('-inf'))
        def inOrder(root):
            nonlocal first, second, pre
            if not root: return
            inOrder(root.left)
            # If first element not found, assign it to prevElement 
            if not first and pre.val >= root.val:
                first = pre
            # If first element is found, assign the second element to the root
            if first and pre.val >= root.val:
                second = root
            pre = root
            inOrder(root.right)
        
        inOrder(root)
        first.val, second.val = second.val, first.val