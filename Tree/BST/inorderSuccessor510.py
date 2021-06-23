"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        
Three cases:

node has a right child, then its successor is its leftmost leaf node
node has no right child, then its successor must be the nearest ancestor who has a left child.
no successor if none of the above two cases hold
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # node has a right child
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        # node has no right child
        # if node.parent and node.parent.left == node: this is wrong
        #     return node.parent
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent
        # no successor if none of the above two cases hold
        return None