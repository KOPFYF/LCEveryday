# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        # loop to the tail and count length
        node = head
        cnt = 1 # not zero
        while node.next:
            cnt += 1
            node = node.next
        node.next = head # now it's a cricle
        
        # new tail: (n - k % n - 1)-th node
        # new head: new tail + 1
        new_tail = head
        for _ in range(cnt - k % cnt - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
        