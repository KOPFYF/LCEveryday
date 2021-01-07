class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Same as predict winner
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return piles[i]
            x, y = dfs(i + 1, j), dfs(i, j - 1)
            
            return max(piles[i] - x, piles[j] - y)
        
        return dfs(0, len(piles) - 1) >= 0