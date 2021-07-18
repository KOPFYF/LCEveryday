class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        seen = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if (cur, i, -1) in seen or (cur, -1, j) in seen or (cur, i//3, j//3) in seen:
                        return False
                    seen.add((cur, i, -1))
                    seen.add((cur, -1, j))
                    seen.add((cur, i//3, j//3))
        return True