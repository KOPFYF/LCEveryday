"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # iteration
        if not root: return
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root
        # inorder
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right
        
        # recursion
        if not root:
            return None
        
        self.dummy = Node(-1)
        self.prev = self.dummy
        self.inorder(root)
        
        # connect 1 and 5, dummy.right = 1, after dfs, prev = 5
        self.dummy.right.left, self.prev.right = self.prev, self.dummy.right
        return self.dummy.right
    
    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        # connect 1-2-3-4-5 bidirectinally using inorder traverse
        self.prev.right, root.left, self.prev = root, self.prev, root
        self.inorder(root.right)
        