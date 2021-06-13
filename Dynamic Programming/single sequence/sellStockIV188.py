class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # if use n + 1, just set init buy as -inf
        # if use n, just set init buy as -prices[0]


        n = len(prices)
        if k > n // 2: # avoid TLE, make maximum number of transactions
            cur = 0
            for i in range(1, n):
                cur += max(0, prices[i] - prices[i - 1])
            return cur
        
        buy, sell = [float("-inf")] * (k + 1), [0] * (k + 1)
        for price in prices:
            for kk in range(1, k + 1):
                buy[kk] = max(buy[kk], sell[kk-1] - price)
                sell[kk] = max(sell[kk], buy[kk] + price)
        return sell[-1]
        
        
        
        # not work for now
        # 2*k states, buy1 -> sell1 -> buy2 -> sell2 ...
        #.             0        1       2.      3
        n = len(prices)
        dp = [[float('-inf')] * 2 * k for _ in range(n)]
        dp[0][0] = -prices[0] # buy1 for prices[0]
        
        for i in range(1, n):
            for kk in range(1, 2*k):
                if kk == 0:
                    dp[i][0] = max(0 - prices[i], dp[i - 1][0]) 
                elif kk % 2: # odd is sell
                    dp[i][kk] = max(dp[i - 1][kk-1] + prices[i], dp[i - 1][kk])
                else: # buy
                    dp[i][kk] = max(dp[i - 1][kk-1] - prices[i], dp[i - 1][kk])
        print(dp)
        return max(dp[-1] + [0]) 