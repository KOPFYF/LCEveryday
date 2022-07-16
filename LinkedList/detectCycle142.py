# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
For anyone confused why slow and fast are equidistant (travelling forward) from the meeting point to the entry point

Let's further break down C, given the following:
L2 = distance from entry to meeting point
L3 = distance from meeting point to entry (forward in loop)
then we have C = L2 + L3

We already have L1 = (n - 1) C + (C - L2) from ngcl's excellent explanation.

(n - 1)C
This is n-1 traversals of the loop distance C

C - L2
Substitute for C: (L2 + L3) - L2 => L3

Finally we get: L1 = (n - 1)C + L3.

Therefore, distance from head to entry is the same as the forward distance (following the loop) from meeting point to entry + n - 1 loop traversals

'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's Tortoise and Hare
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: 
                break
        else: 
            return None  # if not (fast and fast.next): return None
        
        while head != slow:
            head, slow = head.next, slow.next
        return head