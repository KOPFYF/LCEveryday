class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # heap will pop out the biggest profit event
        # sort by capital, and greedily process in capital increasing order
        
        hq = [] # max heap stores profit
        events = sorted(zip(profits, capital), key=lambda x:x[-1]) # sort by capital
        i, n = 0, len(events)
        for _ in range(k):
            while i < n and events[i][1] <= w: # push all candidates
                heapq.heappush(hq, -events[i][0])
                i += 1
            if hq: # greedily pop out the candidate with the biggest profit
                w -= heapq.heappop(hq) # profit stores as neg, so minus. w is increasing too
        return w