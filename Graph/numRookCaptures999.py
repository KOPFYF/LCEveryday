class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x0, y0 = i, j
        res = 0
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            # chooses one of four cardinal directions
            x, y = x0 + i, y0 + j
            while 0 <= x < 8 and 0 <= y < 8:
                # 1. reaches the edge of the board, 
                # 2. captures a black pawn, 
                # 3. is blocked by a white bishop
                if board[x][y] == 'p': # 2
                    res += 1
                if board[x][y] != '.': #2 & 3
                    break
                x, y = x + i, y + j
        return res