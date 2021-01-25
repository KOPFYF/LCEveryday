class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # Dijkstra, O(mnlogmn)
        m, n = len(grid), len(grid[0])
        dirs = {1:(0, 1), 2:(0, -1), 3:(1, 0), 4:(-1, 0)}
        hq, seen = [(0, 0, 0)], defaultdict(lambda:inf)
        while hq:
            cost, i, j = heapq.heappop(hq)
            if (i, j) == (m-1, n-1): 
                return cost
            for s, d in dirs.items():
                x, y = i + d[0], j + d[1]
                if m > x >= 0 <= y < n:
                    c = 1 - (s == grid[i][j]) # if dir not match, cost++
                    if seen[(x, y)] > c + cost:
                        seen[(x, y)] = c + cost
                        heapq.heappush(hq, (c + cost, x, y))
                    