"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
     
        cur     ----------->        cur.next
      /      \\                      /       \
cur.left -> cur.right -> cur.right.next ->


"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cur = root
        nxt = root.left # point to the nxt level

        while cur.left :
            cur.left.next = cur.right # connect left & right
            if cur.next: # horizontal scan
                cur.right.next = cur.next.left
                cur = cur.next
            else: # till the end, skip to the nxt level
                cur = nxt
                nxt = cur.left # point to the nxt nxt level
        