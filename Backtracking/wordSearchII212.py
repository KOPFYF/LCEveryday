class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words, m, n = set(words), len(board), len(board[0])
        def dfs(i, j, l, word):
            if word[l] != board[i][j]: return False
            if l + 1 == len(word): return True
            
            tmp = board[i][j]
            board[i][j] = '#'
        
            res = False
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    res = res or dfs(x, y, l + 1, word)
            board[i][j] = tmp
            return res
        
        return set(word for word in words for i in range(m) for j in range(n) if dfs(i, j, 0, word))
    
        # for word in words:
        #     for i in range(m):
        #         for j in range(n):
        #             if dfs(i, j, 0, word):
        #                 res.add(word)
        # return list(res)