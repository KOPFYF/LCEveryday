# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle, middle will be the slow pointer
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse the 2nd part
        prev, cur = None, slow.next
        while cur:
            nxt = cur.next
            cur.next = prev # reverse
            prev = cur
            cur = nxt
        slow.next = None
        
        # merge 2 lists
        head1, head2 = head, prev
        while head2:
            nxt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nxt