class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum = [0]
        for num in stones:
            presum.append(num + presum[-1])
        
        n = len(stones)
        
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            a = presum[j + 1] - presum[i + 1] - dfs(i + 1, j)
            b = presum[j] - presum[i] - dfs(i, j - 1)
            return max(a, b)
        
        res = dfs(0, len(stones) - 1)
        dfs.cache_clear() # without this line it would cause TLE
        
        return res
    
    '''
    https://leetcode.com/problems/stone-game-vii/discuss/970313/Unfriendly-to-python-why-my-python-O(n2)-topdown-dp-got-MLE
    Python TLE soln:
    use list data structure
    del the data structure at the end of a method
    call the .clear() method of that data structure
    combine @lru_cache(None) with .cache_clear()
    change to a space 1d dp algorithm if possible
    change to a bottom-up dp
    change to c++ or java
    '''


class Solution_TLE:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum = [0]
        for num in stones:
            presum.append(num + presum[-1])
        
        n = len(stones)
        
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            a = presum[j + 1] - presum[i + 1] - dfs(i + 1, j)
            b = presum[j] - presum[i] - dfs(i, j - 1)
            return max(a, b)
        
        return dfs(0, len(stones) - 1)