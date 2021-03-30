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
        # inorder traversal sol - recursion 
        if not root:
            return
        self.head, self.prev = None, None
        
        self.inorder(root)
        # print(self.head.val, self.prev.val) # 1, 5
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head
        
    def inorder(self, cur):
        if not cur:
            return
        self.inorder(cur.left)
        if self.prev:
            self.prev.right = cur
            cur.left = self.prev
        else: 
            # at the head, prev inited as none
            self.head = cur
        self.prev = cur
        # print(self.prev.val)
        self.inorder(cur.right)


class Solution2:
    def treeToDoublyList(self, root):
        if not root: return
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right