class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n)/O(1)
        # 4 states, buy1 -> sell1 -> buy2 -> sell2
        # init value: set buy to -inf, set sell to 0
        n = len(prices)
        buy1, buy2, sell1, sell2 = -prices[0], float('-inf'), float('-inf'), float('-inf')
        
        for i in range(1, n):
            buy1 = max(0 - prices[i], buy1) # it could be not buy i=0
            sell1 = max(buy1 + prices[i], sell1)
            buy2 = max(sell1 - prices[i], buy2)
            sell2 = max(buy2 + prices[i], sell2)
        
        # print(dp)
        return max(sell2, 0) # no need to complete 2 trans
    
        # O(n)/O(n)
        # 4 states, buy1 -> sell1 -> buy2 -> sell2
        # init value: set buy to -inf, set sell to 0
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]
        dp[0][1] = dp[0][2] = dp[0][3] = float('-inf')
        dp[0][0] = -prices[0] # buy1 for prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(0 - prices[i], dp[i - 1][0]) # it could be not buy i=0
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1] - prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i - 1][2] + prices[i], dp[i - 1][3])
        
        # print(dp)
        return max(dp[-1] + [0]) # no need to complete 2 trans


        # O(n)/O(n)
        # 4 states, buy1 -> sell1 -> buy2 -> sell2
        # init value: set buy to -inf, set sell to 0
        n = len(prices)
        dp = [[float('-inf')] * 4 for _ in range(n)]
        # dp[0][1] = dp[0][2] = dp[0][3] = float('-inf')
        dp[0][0] = -prices[0] # buy1 for prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(0 - prices[i], dp[i - 1][0]) # it could be not buy i=0
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1] - prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i - 1][2] + prices[i], dp[i - 1][3])
        
        # print(dp)
        return max(dp[-1] + [0]) # no need to complete 2 trans
        