class Solution:
    def stoneGameIII(self, piles: List[int]) -> str:
        n = len(piles)

          
        @lru_cache(None)
        def dfs(i):
            if i >= n: 
                return 0
            
            res, presum = float('-inf'), 0 
            for x in range(1, 4):
                if i + x - 1 >= n: # index overflow
                    break
                presum += nums[i + x - 1]    
                res = max(res, presum - dfs(i + x))
            return res
        
        return dfs(0, 1)