class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ratio = [(float(w)/q, q) for w, q in zip(wage, quality)]
        ratio.sort() # sort by ratio inc cuz we want small ratio
        hq = [] # max heap storing -quality, pop out big q
        qsum, res = 0, float('inf')

        # For every ratio, we find the minimum possible total quality of K workers.
        for r, q in ratio:
            heapq.heappush(hq, -q)
            qsum += q
            if len(hq) > K:
                nq = -heapq.heappop(hq) # pop out big quality cuz we need min wage
                qsum -= nq
            if len(hq) == K:
                res = min(res, r * qsum)
            
        return res