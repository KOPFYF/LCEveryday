# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # iteration
        if not head or not head.next:
            return head
        second = head.next 
        pre = ListNode(0)
        while head and head.next:
            nxt = head.next
            head.next = nxt.next
            nxt.next = head
            pre.next = nxt
            head = head.next
            pre = nxt.next
        return second
        
        # recursion
        # head -> tmp -> ... ->
        # tmp -> head -> ... -> 
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next) 
            tmp.next = head
            return tmp # return new head
        return head # len = 0 or 1