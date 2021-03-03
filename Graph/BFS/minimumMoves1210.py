

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        H, V = 0, 1  # horizontal or vertical
        # helper funcs, with tail positon(x, y)
        def canRight(x, y, hv):
            if hv == H:
                return y + 2 < n and grid[x][y + 2] == 0
            else:
                return y + 1 < n and grid[x][y + 1] == grid[x + 1][y + 1] == 0

        def canDown(x, y, hv):
            if hv == H:
                return x + 1 < n and grid[x + 1][y] == grid[x + 1][y + 1] == 0
            else:
                return x + 2 < n and grid[x + 2][y] == 0

        def canRotateCW(x, y, hv):
            if hv == V: return False
            return x + 1 < n and grid[x + 1][y] == grid[x + 1][y + 1] == 0

        def canRotateCCW(x, y, hv):
            if hv == H: return False
            return y + 1 < n and grid[x][y + 1] == grid[x + 1][y + 1] == 0

        start = (0, 0, H)
        end = (n - 1, n - 2, H)
        cur_level = {start}
        moves = 0
        visited = set()
        while cur_level:
            next_level = set() 
            for cur in cur_level:
                visited.add(cur)
                x, y, hv = cur
                if canRight(x, y, hv) and (x, y+1, hv) not in visited:
                    next_level.add((x, y+1, hv))
                if canDown(x, y, hv) and (x+1, y, hv) not in visited:
                    next_level.add((x+1, y, hv))
                if canRotateCW(x, y, hv) and (x, y, V) not in visited:
                    next_level.add((x, y, V))
                if canRotateCCW(x, y, hv) and (x, y, H) not in visited:
                    next_level.add((x, y, H))
            if end in next_level:
                return moves + 1
            cur_level = next_level
            moves += 1
        return -1
        
        