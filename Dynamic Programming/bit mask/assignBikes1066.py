class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        # top down bitmask
        def dist(x, y):
            return abs(x[0]- y[0]) + abs(x[1] - y[1])
        
        def calculate(i, visited, cache):
            
            if i == len(workers): return 0
            
            if (i, visited) in cache:
                return cache[(i, visited)]
            
            ans = float('inf')
            for j, bike in enumerate(bikes):
                if visited & (1 << j): 
                    continue
                ans = min(ans, dist(bike, workers[i]) + calculate(i+1, visited | 1 << j, cache))
            cache[(i, visited)] = ans
            return ans
        
        return calculate(0, 0, {})
        
        
        # Bottom up DP, bitmask
        def Manhattan(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        
        m, n = len(workers), len(bikes)
        dp = [[float('inf')] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0
        for i, worker in enumerate(workers):
            for mask in range(1 << n):
                for j, bike in enumerate(bikes):
                    if not mask & (1 << j): # bike j not used
                        nxt_mask = mask | (1 << j)
                        dp[i + 1][nxt_mask] = min(dp[i + 1][nxt_mask], dp[i][mask] + Manhattan(i, j))
        return min(dp[-1])
                
        
        
        # Dijstra, 
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
                    
            