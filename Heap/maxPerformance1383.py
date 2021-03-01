class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        # heap. O(nlogn + nlogk) / O(n)
        # We keep the queue with maximum size of k.
        # Each time when we introduce a new engineer,
        # we need only O(logK) to find the smallest speed in the team now.
        hq = []
        res, cumsum = 0, 0
        for e, s in sorted(zip(efficiency, speed), reverse=True): # max eff, max speed first
            heapq.heappush(hq, s)
            cumsum += s
            if len(hq) > k:
                cumsum -= heapq.heappop(hq)
            res = max(res, cumsum * e)
            
        return res % (10**9 + 7)
    
        # Insort O(n^2) / O(n)
        hq = []
        res, cumsum = 0, 0
        for e, s in sorted(zip(efficiency, speed), reverse=True): # max eff, max speed first
            bisect.insort(hq, -s)
            cumsum += s
            if len(hq) > k:
                cumsum += hq.pop()
            res = max(res, cumsum * e)
            
        return res % (10**9 + 7)
        
        
        