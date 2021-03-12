class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def helper(x, y):
            # -2: change from 1 to 0
            # -1: change from 0 to 1
            change = 0
            for nx in (x - 1, x, x + 1):
                for ny in (y - 1, y, y + 1):
                    if (nx, ny) == (x, y) or nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    change += 1 if board[nx][ny] in (1, -2) else 0
            return change
        
        for i in range(m):
            for j in range(n):
                change = helper(i, j)
                if board[i][j] == 1 and (change < 2 or change > 3):
                    board[i][j] = -2 # turn 1 to 0
                if board[i][j] == 0 and change == 3:
                    board[i][j] = -1 # turn 0 to 1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] < 0:
                    board[i][j] += 2
                
                