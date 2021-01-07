class Solution_bu:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # https://leetcode.com/problems/last-stone-weight-ii/discuss/402213/Python-solution-based-on-0-1-Knapsack
        # find a partition of numbers in the array into two subsets, which have the least amount of differenc in their summations.
        total = sum(stones)
        Max_weight = int(total / 2)
        current = (Max_weight + 1) * [0]
        
        # weights of the rocks is maximized and their total weight does not exceed half 
        for v in stones:
            for w in range(Max_weight, -1, -1):
                if w - v >= 0:
                    current[w] = max(v + current[w - v], current[w])
            
           
        return total - 2 * current[-1]


class Solution_td:
    def lastStoneWeightII(self, stones: List[int]) -> int:    
        @lru_cache(None)
        def dfs(i, sum1, sum2):
            if i >= len(stones):
                return abs(sum1 - sum2)
            
            left = dfs(i + 1, sum1 + stones[i], sum2)
            right = dfs(i + 1, sum1, sum2 + stones[i])
            
            return min(left, right)
        
        return dfs(0, 0, 0)