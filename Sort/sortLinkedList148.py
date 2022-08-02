# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort 
        # O(nlogn)/O(logn)
        # Since the problem is recursive, we need additional space to store the recursive call stack. The maximum depth of the recursion tree is logn
        if not head or not head.next:
            return head
        
        mid = self.findMid(head)
        right = self.sortList(mid.next)
        mid.next = None # break in the middle
        left = self.sortList(head)
        return self.merge(left, right)
    
    def findMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
        return slow
    
    def merge(self, h1, h2):
        dummy = ListNode()
        cur = dummy
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next 
            else:
                cur.next = h2
                h2 = h2.next 
            cur = cur.next 
        
        cur.next = h1 or h2
        return dummy.next