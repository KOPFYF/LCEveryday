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
        # type1: node.left.next = node.right
        # type2: node.right.next = node.next.left
        # O(n) / O(1)
        if not root:
            return root
        
        leftmost = root
        while leftmost.left: # break if we reach final level
            head = leftmost
            while head:
                # type 1
                head.left.next = head.right
                # type 2
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
            
        return root
            
        
        
        
        # BFS O(n) /O(n)
        if not root:
            return root
        
        bfs = deque([root])
        while bfs:
            n = len(bfs)
            for i in range(n):
                node = bfs.popleft()
                if i < n - 1:
                    node.next = bfs[0]
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return root