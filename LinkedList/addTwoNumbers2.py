# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carrier = 0
        dummy = cur = ListNode()
        while l1 or l2 or carrier:
            if l1:
                carrier += l1.val
                l1 = l1.next
            if l2:
                carrier += l2.val
                l2 = l2.next
            cur.next = ListNode(carrier % 10)
            cur = cur.next
            carrier //= 10
            
        return dummy.next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        cur, carrier = 0, 0
        while l1 or l2:
            cur = carrier
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            carrier = cur // 10
            cur = cur % 10
            node.next = ListNode(cur)
            node = node.next
        if carrier:
            node.next = ListNode(carrier)
        return dummy.next