class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        1   5  9
        10 11 13
        12 13 15
        
        8

        '''
        # minheap, O(klogk) / O(k)
        n = len(matrix)
        hq = []
        for i in range(min(k, n)):
            heapq.heappush(hq, (matrix[i][0], i, 0))
        res = -1
        for _ in range(k):
            res, x, y = heapq.heappop(hq)
            if y + 1 < n:
                heapq.heappush(hq, (matrix[x][y + 1], x, y + 1))
        return res
            
        
        
        # O((m+n) * logD)
        # bisect the matrix value directly, flatten it into a 1 d list
        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                # l -(t)- mid -- r
                l = mid + 1
            else:
                r = mid
        return l

        
        
        
        
        
        