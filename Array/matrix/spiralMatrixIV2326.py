# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        u, d, l, r = 0, m - 1, 0, n - 1
        
        while head:
            for i in range(l, r + 1):
                if head:
                    res[u][i] = head.val
                    head = head.next
            u += 1
            if u > d: break
                
            for i in range(u, d + 1):
                if head:
                    res[i][r] = head.val
                    head = head.next
            r -= 1
            if l > r: break
            
            for i in range(r, l - 1, -1):
                if head:
                    res[d][i] = head.val
                    head = head.next
            d -= 1
            if u > d: break
            
            for i in range(d, u - 1, -1):
                if head:
                    res[i][l] = head.val
                    head = head.next
            l += 1
            if l > r: break
        
        return res