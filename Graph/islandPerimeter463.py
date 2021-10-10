class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # check two neighbors (LEFT and UP)
        # O(mn) / O(1)
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i-1][j] == 1: # up is island too
                        res -= 2 # one from each side
                    if j > 0 and grid[i][j-1] == 1:
                        res -= 2
        return res


class Solution1:
    # DFS, count water block instead of island
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # exactly one island, so...
        def sum_adjacent(i, j):
            # focus on water
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                    # if it's edge(index overflows) or it's water(cell=0), +1
                    res += 1
            return res

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += sum_adjacent(i, j)
        return count