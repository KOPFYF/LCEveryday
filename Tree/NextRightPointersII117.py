"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # O(n) / O(1)
        if not root:
            return root
        node = root # parent level 
        while node:
            cur = dummy = Node(0) # inter-level
            while node:
                if node.left:
                    cur.next = node.left
                    cur = cur.next
                if node.right:
                    cur.next = node.right
                    cur = cur.next
                node = node.next # finish current node
            node = dummy.next # to the next level
        return root
        
        
        
        # O(n) / O(n)
        if not root:
            return root
        
        bfs = deque([root])
        while bfs:
            n = len(bfs)
            for i in range(n):
                node = bfs.popleft()
                if i < n - 1: # when i = n - 1 it's the last node in cur level, no next then
                    node.next = bfs[0]
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return root