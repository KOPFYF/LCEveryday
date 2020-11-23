class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top down DP
        @lru_cache(None)
        def dfs(n):
            if n < 0: return -1
            if n == 0: return 0
            
            res = float('inf')
            for coin in coins:
                subprob = dfs(n - coin)
                if subprob != -1: 
                    res = min(res, subprob + 1)
            return res if res != float('inf') else -1
        
        return dfs(amount)


class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # Bottom UP 2D DP
        # dp[i][j] using coin[:i] to achieve amt j
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]  
                print(i, j, dp[i][j])
                
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
        
        # Bottom UP 1D DP
        dp = [0] + [float('inf')] * amount
        
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] = min(dp[i], dp[i - coin] + 1)
        
        for coin in coins:
            for i in range(amount + 1):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1