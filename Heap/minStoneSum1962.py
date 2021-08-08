class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # greedy & heap
        hq = [-p for p in piles] # max heap, store neg
        heapq.heapify(hq)
        res = 0
        while k > 0 and hq:
            maxp = -heapq.heappop(hq)
            nxtp = maxp // 2
            res += nxtp
            
            if nxtp - maxp:
                heapq.heappush(hq, nxtp - maxp)
            k -= 1
        return sum(piles) - res
            