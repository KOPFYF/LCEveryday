class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # sliding win
        # overdo it, squeeze to median then recover to radius
        
        # p[i]: the position of i-th 1
        p = [i for i, v in enumerate(nums) if v]
        res, n, presum = float('inf'), len(p), [0] * (len(p) + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + p[i]
            
        if k & 1: # odd
            radius = (k - 1) // 2
            for i in range(radius, n - radius):
                # i-radius ... i ... i+radius
                right = presum[i + radius + 1] - presum[i + 1]
                left = presum[i] - presum[i - radius]
                res = min(res, right - left)
            return res - radius * (radius + 1)
        else: # even
            # move radius to i (moving to i+1 is also OK)
            radius = (k - 2) // 2
            for i in range(radius, n - radius - 1):
                # i-radius ... i ... i+radius
                right = presum[i + radius + 2] - presum[i + 1]
                left = presum[i] - presum[i - radius]
                res = min(res, right - left - p[i])
            return res - radius * (radius + 1) - (radius + 1)
            
        
        
        