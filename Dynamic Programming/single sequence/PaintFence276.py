class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0: 
            return 0
        if n == 1: 
            return k
        
        diff = [0] * n
        same = [0] * n
        same[0] = same[1] = k
        diff[0] = k
        diff[1] = k * (k - 1)
        
        for i in range(2, n):
            same[i] = diff[i-1]
            diff[i] = (k - 1) * same[i-1] + (k - 1) * diff[i-1]
        
        return same[-1] + diff[-1]