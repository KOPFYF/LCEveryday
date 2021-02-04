class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS, time O(m^2n^2), space O(mn)
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(x, y, word):
            if not word:
                return True
            tmp, board[x][y] = board[x][y], '#' # mask off
            res = False
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[0] \
                    and dfs(nx, ny, word[1:]):
                        res = True
                        break
            board[x][y] = tmp # recover
            return res
        
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and dfs(i, j, word[1:]):
                    return True
        return False