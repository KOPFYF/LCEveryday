# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        '''
        When we are at the line pre.next.next = cur the LL looks like this for [1,2,3,4,5] m = 2, n = 4

        1 -> 2 <- 3 <- 4    5
        pre            rev

        Note that there is no connection between 4 and 5, here pre is node 1, reverse is node 4, cur is node 5; 
        So pre.next.next = cur is basically linking 2 with 5; pre.next = reverse links node 1 with node 4.
        
        '''
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            nxt = cur.next
            cur.next = reverse
            reverse = cur
            cur = nxt

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next