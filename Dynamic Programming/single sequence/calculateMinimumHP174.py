class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # dp O(mn)/O(mn)
        # dp[i][j] = minimum health level required to reach the princess when entering (i, j)
        # If at least one of these two numbers is negative, it means that we can survive just with 1 hp
        # If both this numbers are positive, we need to take the mimumum of them
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # min to take the cheapest way
                # minus dungeon[i][j] bcz we optimize in opposite dir
                # max to cap by 1, so to avoid die cases(hp drops to 0) 
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        
        return dp[0][0]
    
    
        @functools.lru_cache(None)
        def dp(i,j):
            if (i,j) in ((m-1, n),(m, n-1)): 
                return 1
            if i == m or j == n: 
                return math.inf
            return max(min(dp(i+1,j), dp(i,j+1)) - dungeon[i][j], 1)

        m, n = len(dungeon), len(dungeon[0])
        return dp(0,0)