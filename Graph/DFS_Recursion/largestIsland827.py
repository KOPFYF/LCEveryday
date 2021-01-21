class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # DfS, O(N^2)/O(N^2)
        # Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
        # Loop every cell == 0, check its connected islands and calculate total islands area.
        N = len(grid)
        
        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j
        
        def dfs(x, y, index):
            # return connected area, index is the id of that component
            res = 1
            grid[x][y] = index # set grid to its id
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res 
        
        # DFS every island and give it an index of island
        index = 2 # index starts from 2 because 1 is used
        areas = {0: 0}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1
        print(areas) # [[1,0],[0,1]], {0: 0, 2: 1, 3: 1}
        print(grid) # [[2, 0], [0, 3]]

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0: # candidate
                    possible = set(grid[i][j] for i, j in move(x, y))
                    print(possible) # {2, 3}
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res
        
        
        