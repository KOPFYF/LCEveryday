class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        def dfs(i, j):
            board[i][j] = '*'
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == '1':
                    dfs(x, y)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res