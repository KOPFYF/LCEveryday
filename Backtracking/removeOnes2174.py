class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.res = float('inf')
        seen = set()
        
        def dfs(flips):
            pos = [(i, j) for i in range(m) for j in range(n)
                  if grid[i][j] == 1 and ('r', i) not in seen 
                  and ('c', j) not in seen]
            if not pos: # all zero
                self.res = min(self.res, flips)
            
            # backtracking, flip (i, j)
            for i, j in pos:
                seen.add(('r', i))
                seen.add(('c', j))  
                dfs(flips + 1)
                seen.remove(('r', i))
                seen.remove(('c', j))
        
        dfs(0)
        
        return self.res