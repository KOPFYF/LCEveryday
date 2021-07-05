# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # no cycles, 2 ptrs, O(m + n)/O(1)
        # worst case, each list is traversed twice giving 2(m + n)
        
        # proof: a + c + b = b + c + a
        # if itersect, it must meet and break the while loop
        # else, pa will be null and both of them reach ends finally
        # if a & b have different len, then we will stop the loop after second iteration
        
        pa, pb = headA, headB
        
        while pa != pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        return pa
            