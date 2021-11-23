class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # O(mn) / O(mn)
        rows, cols = [], []
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    rows.append(x)
        
        for y in range(n):
            for x in range(m):
                if grid[x][y] == 1:
                    cols.append(y)
        
        # rows.sort() # O(mnlogmn)/O(mn), avoid sort to make it faster
        # cols.sort()
        
        med_x = rows[len(rows)//2] 
        med_y = cols[len(cols)//2]
        
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    res += abs(x - med_x) + abs(y - med_y)
        return res