'''
heapreplace(a, x) returns the smallest value originally in a regardless of the value of x, while, as the name suggests, heappushpop(a, x) pushes x onto a before popping the smallest value. Using your data, here's a sequence that shows the difference:
>>> from heapq import *
>>> a = [2,7,4,0,8,12,14,13,10,3,4]
>>> heapify(a)
>>> b = a[:]
>>> heappushpop(a, -1)
-1
>>> heapreplace(b, -1)
0
'''

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        '''
This optimization evaluates (2*K - 1) items.

Keep a pool of K minimum values seen so far.
Remove smallest item K-1 times (-1 to keep kth smallest on heap).
When you remove that smallest value, add it's successor (same numerator, next smallest denominator).
This newly added item is still in the range of [smallest : 2*K - 1 smallest] items.
Since, it's on a minHeap after K-1 pops of the pool of 2*K-1 smallest items the Kth smallest will be on the top of the heap.
        '''
        # find the kth smallest element of (n-1) sorted list
        heap = [(A[i] / A[-1], i, len(A) - 1) for i in range(min(len(A) - 1, K))]

        for _ in range(K-1):  # only pop k times
            _, i, j = heap[0]
            # j - 1 > i, shrink right pointer
            heapreplace(heap, (A[i]/A[j-1], i, j - 1))

        return [A[heap[0][1]], A[heap[0][2]]]
    
    
        # soln 2
        heap = [(A[0] / A[j], 0, j) for j in reversed(range(max(len(A) - K - 1, 1), len(A)))]

        for _ in range(K-1):
            _, i, j = heap[0]
            if i < len(A) - 1:
                heapreplace(heap, (A[i+1]/A[j], i+1, j))

        return [A[heap[0][1]], A[heap[0][2]]]
