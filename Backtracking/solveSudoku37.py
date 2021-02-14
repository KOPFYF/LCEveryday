class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x, y):
            tmp = board[x][y]
            board[x][y] = 'D'
            for i in range(9):
                if board[i][y] == tmp:
                    return False
            for j in range(9):
                if board[x][j] == tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x//3) * 3 + i][(y//3) * 3 + j] == tmp:
                        return False
            board[x][y] = tmp
            return True
        
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k # try all numbers
                            if isValid(i, j) and dfs(board):
                                return True 
                            board[i][j] = '.'
                        return False # no ans after trying all numbers
            return True
        dfs(board)