class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1] # suffix sum
          
        @lru_cache(None)
        def dfs(i, M):
            if i + 2 * M >= n: # take all the left ones
                return piles[i]
            res = float('inf') # min opponent's gain
            for x in range(1, 2 * M + 1):
                res = min(res, dfs(i + x, max(M, x)))
            return piles[i] - res
        
        return dfs(0, 1)


class Solution2(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        return self.dp(piles, len(piles), 0, 1, {})

    def dp(self, piles, n, i, m, memo):
        if i >= n:
            return 0
        if i + 2 * m >= n:
            return sum(piles[i:])

        if (i, m) in memo:
            return memo[(i, m)]

        total = sum(piles[i:])
        score = 0
        for x in range(1, 2 * m + 1):
            opponent = self.dp(piles, n, i + x, max(x, m), memo)
            score = max(score, total - opponent)

        memo[(i, m)] = score
        return score