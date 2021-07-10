"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = defaultdict(lambda: Node(0)) # store the nodes
        d[None] = None # if a node's next/random is None, 
        
        cur = head
        while cur:
            d[cur].val = cur.val
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        
        return d[head]