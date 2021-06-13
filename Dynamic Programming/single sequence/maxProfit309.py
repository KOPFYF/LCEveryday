class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state 0: cool down/rest
        # state 1: buy it
        # state 2: sell it
        # s0[0] = 0; // At the start, you don't have any stock if you just rest
        # s1[0] = -prices[0]; // After buy, you should have -prices[0] profit. Be positive!
        # s2[0] = INT_MIN; // Lower base case
        
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][1], dp[0][2] = -prices[0], float('-inf')
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][2], dp[i-1][0])  
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1]) 
            dp[i][2] = dp[i-1][1] + prices[i]
        # print(dp)
        return max(dp[-1])
        
        
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)