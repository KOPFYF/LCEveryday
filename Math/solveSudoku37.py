class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(i, j):
            cur = board[i][j]
            board[i][j] = '#'
            for ii in range(9):
                if board[ii][j] == cur:
                    return False
            for jj in range(9):
                if board[i][jj] == cur:
                    return False
            for di in range(3):
                for dj in range(3):
                    ni, nj = (i // 3) * 3 + di, (j // 3) * 3 + dj # // 3 then * 3
                    if board[ni][nj] == cur:
                        return False
            board[i][j] = cur
            return True
        
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in list('123456789'):
                            board[i][j] = num
                            if check(i, j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False # try all digits but fail
            return True # try all cells and success
        
        dfs(board)