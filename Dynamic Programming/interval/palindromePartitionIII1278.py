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



class Solution2:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k:
            return 0
        
        cost = [[0] * n for _ in range(n)]
        dp = [[0] * n for _ in range(k+1)]
        
        for i in range(n):
            cost[i][i] = 0
        
        for i in range(n):
            for j in range(n):
                cost[i][j] = self.get_cost(s, i, j)
        
        # Split array 
        for i in range(n):
            dp[1][i] = cost[0][i]
        
        for i in range(2, k+1):
            for j in range(i-1, n):
                min_cost = float('inf')
                for split in range(j - 1, i - 3, -1):
                    min_cost = min(min_cost, dp[i-1][split] + cost[split+1][j])
                
                dp[i][j] = min_cost
        
        return dp[k][n-1]
        
    def get_cost(self, s, i, j):
        cost = 0
        while i < j:
            if s[i] != s[j]:
                cost += 1
            i += 1
            j -= 1
        return cost