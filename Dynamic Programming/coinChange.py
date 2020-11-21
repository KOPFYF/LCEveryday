class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
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

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
        
        # 1D DP
        dp = [0] + [float('inf')] * amount
        
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] = min(dp[i], dp[i - coin] + 1)
        
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1