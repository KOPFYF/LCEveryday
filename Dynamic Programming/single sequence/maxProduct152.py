class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP time O(n), space O(1)
        res = nums[0]
        pmax = pmin = 1
        for i in range(0, len(nums)):
            if nums[i] < 0: # flip if negative
                pmax, pmin = pmin, pmax
            pmax = max(nums[i], pmax * nums[i])
            pmin = min(nums[i], pmin * nums[i])      
            res = max(res, pmax)
            # print(pmax, pmin, res)
            # [2,3,-2,4]
            # 2 2 2
            # 6 3 6
            # -2 -12 6
            # 4 -48 6    
        return res