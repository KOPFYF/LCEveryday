# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = head
        i = 1
        while head:
            if i < m:
                i += 1
            else:
                j = 0
                while j < n and head.next:
                    head.next = head.next.next # skip n times
                    j += 1
                i = 1
            head = head.next
        return dummy