class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dfs(i):
            # return min cost to reach i
            if i <= 1:
                return 0
            tmp1 = dfs(i - 1) + cost[i - 1]
            tmp2 = dfs(i - 2) + cost[i - 2]
            
            return min(tmp1, tmp2)
        
        return dfs(len(cost))