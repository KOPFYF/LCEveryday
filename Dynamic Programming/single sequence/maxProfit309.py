class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state 0: cool down/rest
        # state 1: buy it
        # state 2: sell it
        
        n = len(prices)
        cooldown, buy, sell = 0, -prices[0], float('-inf')
        for i in range(1, n):
            cooldown, buy, sell = max(sell, cooldown), \
                                  max(cooldown - prices[i], buy), \
                                  buy + prices[i]   
        return max(cooldown, sell)
        
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][2], dp[i-1][0])  
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1]) 
            dp[i][2] = dp[i-1][1] + prices[i]
        # print(dp)
        return max(dp[-1])