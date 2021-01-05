class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j - 1)) + 1
        
        return dfs(0, len(s) - 1) <= k