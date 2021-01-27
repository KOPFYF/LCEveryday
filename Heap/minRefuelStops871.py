class Solution:
    def minRefuelStops(self, target: int, cur: int, stations: List[List[int]]) -> int:
        # heap + greedy, O(nlogn)
        # i is the index of next stops to refuel.
        # res is the times that we have refeuled.
        # pq is a priority queue that we store all available gas.
        # *** In every loop ***
        # We add all reachable stop to priority queue.
        # We pop out the largest gas from pq and refeul once.
        # If we can't refuel, means that we can not go forward and return -1
        pq = []
        res, i = 0, 0
        while cur < target:
            while i < len(stations) and stations[i][0] <= cur: # can reach
                heapq.heappush(pq, -stations[i][1]) # max heap, pop out largest gas
                i += 1
            if not pq:
                return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res