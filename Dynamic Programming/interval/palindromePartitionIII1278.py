class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dfs(s, k):
            if len(s) == k: return 0 # base case, no change needed
            if k == 1: # base case, no spilt
                res = sum(s[i] != s[-1-i] for i in range(len(s) // 2))
            else:
                res = float('inf')
                for i in range(1, len(s) - k + 2): 
                    # if k = 2, split once, range(1, len(s))
                    # if k = 3, split twice, range(1, len(s) - 1)
                    # res = min(left no split, right spilt k - 1, res)
                    res = min(dfs(s[:i], 1) + dfs(s[i:], k - 1), res)
            return res
        return dfs(s, k)