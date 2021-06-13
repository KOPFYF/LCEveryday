class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        def Manhattan(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        
        hq = [(0, 0, 0)] # dist, x, y
        seen = set()
        
        while hq:
            dist, i, mask = heapq.heappop(hq)
            if (i, mask) in seen: # i has been processed before
                continue
            seen.add((i, mask))
            if i == len(workers):
                return dist
            for j in range(len(bikes)):
                if not mask & (1 << j): # bike j not taken
                    heapq.heappush(hq, (dist + Manhattan(i, j), i + 1, mask | (1 << j)))