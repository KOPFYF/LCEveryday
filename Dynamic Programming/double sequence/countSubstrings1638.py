class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # dp(i, j, k) means the number of substrings ending at s[i] and t[j] and differed by k (0 or 1) character.
        # O(mn)/O(mn)
        m, n = len(s), len(t)
        
        @lru_cache(None)
        def dfs(i, j, k):
            # base case
            if i < 0 or j < 0 or k < 0:
                return 0
            if k == 0 and s[i] != t[j]:
                return 0
            
            res = 0
            if s[i] == t[j]:
                res += dfs(i - 1, j - 1, k) + (k == 0) # match, but if k used before, +1
            else:
                res += dfs(i - 1, j - 1, k - 1) + 1 # use k once, single char is a valid soln
            return res
               
        cnt = 0
        for i in range(m):
            for j in range(n):
                cnt += dfs(i, j, 1)
        return cnt