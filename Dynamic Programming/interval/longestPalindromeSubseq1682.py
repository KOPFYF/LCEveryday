class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i, j, prev):
            if i >= j:
                return 0
            # use a variable prev to make sure no two consecutive characters are equal
            if s[i] == s[j] and s[i] != prev:
                return dfs(i + 1, j - 1, s[i]) + 2
            return max(dfs(i + 1, j, prev), dfs(i, j - 1, prev))
        
        # TLE return dfs(0, len(s) - 1, '*')
        # You can add dp.cache_clear() before returning the result. 
        # It is something related to the memory that may cause this problem.
        res = dfs(0, len(s) - 1, '*')
        dfs.cache_clear()
        
        return res

# or write memo myself
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        
        def dp(l, r, prev):
            if (l, r, prev) not in memo:
                if l >= r:
                    return 0
                if s[l] == s[r] and (s[l] != prev):
                    return 2 + dp(l + 1, r - 1, s[l])
                memo[(l, r, prev)] = max(dp(l + 1, r, prev), dp(l, r - 1, prev))
            return memo[(l, r, prev)]

        return dp(0, len(s) - 1, '')