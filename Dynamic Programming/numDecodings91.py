class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        leading 0 is illegal
        dp[i] = the number of ways to parse the string s[1: i + 1]
        '''
        n = len(s)
        if not s or s[0] == '0':
            return 0

        @lru_cache(None)
        def dfs(i):
            # how many ways from s[i:]
            # s[i], dfs(i+1) or s[i], s[i+1], dfs(i+2)
            if i == n:
                return 1
            if s[i] == '0':
                return 0 # single 0 is invalid
            res = dfs(i + 1) # init from s[i+1:]
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                res += dfs(i + 2)
            return res
            
            
        return dfs(0)
            