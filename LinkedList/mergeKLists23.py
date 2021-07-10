# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # merge k linked list, O(logk) * O(l1 + l2)
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        # merge 2 linked list iteratively, O(l1 + l2)
        dummy = cur = ListNode()
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next
    
    def merge1(self, l, r):
        # merge 2 linked list recursively
        if not l or not r:
            return l or r
        if l.val < r.val:
            l.next = self.merge(l.next, r)
            return l
        else:
            r.next = self.merge(l, r.next)
            return r
        
        
        # heap
        hq = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(hq)
        dummy = ListNode()
        prev = dummy
        while hq:
            val, idx, node = heapq.heappop(hq)
            prev.next = node
            prev = prev.next # move to next
            if node.next:
                heapq.heappush(hq, (node.next.val, idx, node.next))
        return dummy.next