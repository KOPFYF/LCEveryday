class Solution:
    def minDistance(self, word1: str, word2: str) -> int:       
        @lru_cache(None)
        def dfs(i, j):
            if i == 0 and j == 0:
                return 0
            if i == 0 or j == 0:
                return j or i
            
            return dfs(i - 1, j - 1) if word1[i - 1] == word2[j - 1] \
                    else min(dfs(i, j - 1), dfs(i - 1, j)) + 1
        
        return dfs(len(word1), len(word2))