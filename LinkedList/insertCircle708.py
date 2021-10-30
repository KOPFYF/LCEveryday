"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal, head)
        if not head: # len = 0
            node.next = node
            return node

        # if head == head.next: # len = 1
        #     head.next = node
        #     return head
        
        left, right = head, head.next
        while True:
            # case 1, 2 ends, like 1-2-3 and insert 0/4
            if right.val < left.val and (right.val >= insertVal or left.val <= insertVal):
                break
            # case 2, in between
            elif left.val <= insertVal <= right.val:
                break
            # case 3: the list contains uniform values.
            elif left.next == head: 
                break
            
            left = left.next
            right = right.next
        left.next = node
        node.next = right
        
        return head