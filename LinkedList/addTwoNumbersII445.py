# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        x1, x2 = 0, 0
        while l1:
            x1 = x1*10+l1.val
            l1 = l1.next
        while l2:
            x2 = x2*10+l2.val
            l2 = l2.next
        x = x1 + x2
        
        head = ListNode(0)
        if x == 0: return head
        while x:
            v, x = x%10, x//10
            head.next, head.next.next = ListNode(v), head.next
            
        return head.next
        

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseLinkedList(head):
            prev, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        def add2Nums(l1, l2):
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
        
        res = add2Nums(reverseLinkedList(l1), reverseLinkedList(l2))
        return reverseLinkedList(res)