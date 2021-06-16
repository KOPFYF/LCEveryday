class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        self.dfs(board, i, j, m, n)
        return board
    
    def dfs(self, board, x, y, m, n):
        if board[x][y] != 'E':
            return # recursion only on unrevealed empty square
        dirs = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        cnt = 0
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                cnt += 1
        
        if cnt == 0:
            board[x][y] = 'B' # rule 2
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    self.dfs(board, nx, ny, m, n)
        else:
            board[x][y] = str(cnt) # rule 3, stop early
            return 