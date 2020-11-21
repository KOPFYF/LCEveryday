class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS, time O(m^2n^2), space O(mn)
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(x, y, seen, word):
            if not word:
                return True
            seen.append((x, y))
            res = False
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and \
                (nx, ny) not in seen and board[nx][ny] == word[0]:
                    res = res or dfs(nx, ny, seen, word[1:])
            if not res: seen.pop() # this is vital, give it back if not found anything
            
            return res
        
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and dfs(i, j, [], word[1:]):
                    return True
        return False