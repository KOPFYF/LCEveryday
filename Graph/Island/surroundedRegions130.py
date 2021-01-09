class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return []
        m, n = len(board), len(board[0])
        def dfs(i, j):
            board[i][j] = '*'
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    dfs(x, y)
        
        for i in range(m):
            for j in range(n):
                # loop 'O' on the edge
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    dfs(i, j)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    # eat all 'O' in between
                    board[i][j] = "X"
                elif board[i][j] == "*": 
                    # recover
                    board[i][j] = "O"