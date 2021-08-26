class Solution:
    def numberOfCombinations(self, S: str) -> int:
        '''
        1 <= num.length <= 3500
        backtracking
        
        '''
        # TLE
        mod, n = 10**9 + 7, len(S)
        
        @lru_cache(None)
        def dfs(pos, prev):
            if pos == n:
                return 1
            if S[pos] == '0':
                return 0
            
            res, cur = 0, 0
            for i in range(pos, n):
                cur = int(S[pos:i + 1])
                if cur >= prev: #  non-decreasing 
                    # print(cur, prev)
                    res += dfs(i + 1, cur)
            return res % mod
        
        return dfs(0, 0)