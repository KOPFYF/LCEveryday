"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
'''
If the node has a right child, and hence its successor is somewhere lower in the tree. Go to the right once and then as many times to the left as you could. Return the node you end up with.

Node has no right child, and hence its successor is somewhere upper in the tree. Go up till the node that is left child of its parent. The answer is the parent.
'''
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        '''
        case 1: node has a right child, go to right first then as left as you could
        case 2: node has no right child, go up to the node that is left child of its parent
        '''
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent # could be null -> root.parent


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