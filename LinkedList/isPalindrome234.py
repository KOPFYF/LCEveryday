# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = collections.deque([])
        while head:
            queue.append(head)
            head = head.next
        while len(queue) >= 2:
            if queue.popleft().val != queue.pop().val:
                return False
        return True
    
    
        cur = head
        res = []
        while cur: # and cur.next:
            res.append(cur.val)
            cur = cur.next
        return res == res[::-1]