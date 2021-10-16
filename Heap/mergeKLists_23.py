# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap O(nlogk)
        dummy = cur = ListNode()
        hq = []
        for l in lists:
            if l:
                heapq.heappush((l.val, l)) # heap size always k
        while hq:
            val, node = heapq.heappop(hq) # logk
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(hq, (node.val, node))
        return dummy.next