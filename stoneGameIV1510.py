class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # bottom up DP, O(n*sqrt(n))
        # if there is any k that dp[i - k * k] == false,
        # dp = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        # return dp[-1]
    
        dp = [False]* (n + 1)
        for i in range(n + 1):
            for k in range(1, int(i**0.5) + 1):
                if not dp[i - k * k]:
                    dp[i] = True
                    break # pruning,
        return dp[n]