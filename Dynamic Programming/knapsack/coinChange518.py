class Solution0:
    def change(self, amount: int, coins: List[int]) -> int:
        # top down
        @lru_cache(None)
        # 2 varibales to be cached
        def dfs(n, i):
            if n == 0: return 1
            if n < 0 or i >= len(coins): return 0
            
            take = dfs(n - coins[i], i)
            notake = dfs(n, i + 1)
            return take + notake
        
        return dfs(amount, 0)

class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:        
        # Bottom up     
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[amount]


class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins) 
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dfs(amt, index):
            if amt == 0: # Exact amount, valid combination
                return 1
            if amt<0 or index==n: #Over-shot the amount or ran out of coins, invalid combo
                return 0
           
            curr_res = 0

            for i, coin in enumerate(coins[index:], index):
                curr_res += dfs(amt - coin, i)
            return curr_res

        coins.sort(reverse=True)
        return dfs(amount, 0)