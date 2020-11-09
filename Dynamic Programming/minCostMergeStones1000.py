import functools
class Solution1:
    def mergeStones(self, A: List[int], K: int) -> int:
        # Top Down 3D DP, Time O(N^3/K), Space O(KN^2)
        # State: dp[i][j][m] means the cost needed to merge stone[i] ~ stones[j] into m piles.
        # Function: dp[i][j][1] = dp[i][j][k] + stonesNumber[i][j]
        #           dp[i][j][m] = min(dp[i][mid][1] + dp[mid + 1][j][m - 1])
        # Init: dp[i][i][1] = 0 and dp[i][i][m] = infinity
        # Answer: dp[0][n - 1][1] 
        
        if not A: return 0
        n = len(A)
        inf = float('inf')
        prefix = [0] * (n + 1)
        for i in range(n): 
            prefix[i + 1] = prefix[i] + A[i]
        
        @functools.lru_cache(None)
        def dfs(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                # at least one part should be able to be merged into one single pile
                # total piles: j - i + 1, currently need to merge into m piles, 
                # so the total number of decrement is (j - i + 1 - m) with each step reduce (K - 1)
                # 1, 2, ... (K - 1) ..., m => 1, 2, ... k ..., m
                return inf
            if i == j:
                # dfs end condition, if 2 pointers at the same place, only m = 1 would work
                return 0 if m == 1 else inf
            if m == 1:
                # Base case: we need to merge piles together to 1 pile. 
                # and the last step must be merge K piles 
                # dp[i][j][1] = dp[i][j][k] + stonesNumber[i][j]
                return dfs(i, j, K) + prefix[j + 1] - prefix[i]
            # Each (i, j, m) problem is dfs into (i, mid, 1) + (mid+1, j , m-1)
            # the left half (i, mid, 1) can be resolved by merging K piles consecutively
            # mid jump at step (K - 1) because we can only merge K + (K - 1) * steps of piles into one
            return min(dfs(i, mid, 1) + dfs(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
        
        res = dfs(0, n - 1, 1)
        return res if res < inf else -1
        

class Solution2:
    def mergeStones(self, A: List[int], K: int) -> int:
        # Top Down 2D DP,
        # State: dp[i][j] means the minimum cost needed to merge the range stones[i]...stones[j], 
        #       both i and j inclusive, to the minimum possible piles (this is one or more piles)
        # Compress m by redefine the dp to any possible piles
        # each step we reduce (K - 1) stones, Ni = N - (K - 1)*i
        # eventually need Ni = 1 => N - (K-1) * i == 1 => (N - 1) % (K - 1) == 0
        n = len(A)
        if (n - 1) % (K - 1): 
            return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + A[i]
            
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: 
                return 0
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                # if find a possible step, reduce K piles into 1 (thus crush K - 1 stones)
                res += prefix[j + 1] - prefix[i]
            return res
        return dp(0, n - 1)      
        